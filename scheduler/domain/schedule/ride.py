from dataclasses import dataclass, field
from datetime import datetime, timedelta
from functools import singledispatchmethod

from diator.events import DomainEvent
from diator.requests import Request

from scheduler.domain.common.event_sourced_root_entity import EventSourcedRootEntity
from scheduler.domain.common.identity import Identity
from scheduler.domain.schedule import commands, events
from scheduler.domain.schedule.constants import MAX_RIDE_PERIOD
from scheduler.domain.schedule.delay_report import DelayReport
from scheduler.domain.schedule.enums import DelayReportStatusEnum, RideStatusEnum


@dataclass(kw_only=True, eq=False)
class Ride(EventSourcedRootEntity):
    train_id: Identity
    departure_time: datetime
    arriving_time: datetime
    start_station: str
    end_station: str
    status: RideStatusEnum = field(default=RideStatusEnum.SCHEDULED)
    reports: list[DelayReport] = field(default_factory=list)

    def __post_init__(self) -> None:
        period = self.arriving_time - self.departure_time
        self.assert_value_lt(
            period,
            MAX_RIDE_PERIOD,
            f"Ride period cannot be equal or greater than {MAX_RIDE_PERIOD}",
        )

        self.apply(
            events.RideScheduledEvent(ride_id=self.identity, train_id=self.train_id)
        )

    @singledispatchmethod
    def handle(self, command: Request) -> None:
        ...

    @handle.register
    def _(self, command: commands.UpdateRideStatusCommand) -> None:
        self.assert_values_equal_and(
            command.new_status,
            RideStatusEnum.DEPARTED,
            self.status,
            RideStatusEnum.ARRIVED,
            exc_message="Ride status cannot be changed to 'departed' after it was equal to 'arrived'.",
        )

        previous_status = self.status
        self.status = command.new_status

        self.apply(
            events.RideStatusChangedEvent(
                ride_id=self.identity,
                previous_status=previous_status,
                new_status=self.status,
            )
        )

    @handle.register
    def _(self, command: commands.ReportDelayCommand) -> None:
        delay_report = DelayReport(
            identity=command.report_id,
            reporter_id=command.reporter_id,
            ride_id=command.ride_id,
            comment=command.comment,
            delay_delta=timedelta(minutes=command.delay_minutes),
        )
        self.reports.append(delay_report)

        self.apply(
            events.DelayReportedEvent(
                reporter_id=command.reporter_id,
                report_id=command.report_id,
                ride_id=command.ride_id,
                delay_minutes=command.delay_minutes,
            )
        )

    @handle.register
    def _(self, command: commands.ApproveDelayCommand) -> None:
        selected_report = next(
            (report for report in self.reports if report.identity == command.delay_id),
            None,
        )
        self.assert_is_not_none(selected_report, "Selected report delay is not exist.")

        selected_report.status = DelayReportStatusEnum.APPROVED
        self.arriving_time += selected_report.delay_delta
        self.status = RideStatusEnum.DELAYED

        self.apply(
            events.DelayApprovedEvent(
                report_id=command.delay_id,
                ride_id=self.identity,
                delay_minutes=selected_report.delay_delta.seconds * 60,
            )
        )

    @handle.register
    def _(self, command: commands.DispatchTrainCommand) -> None:
        self.assert_values_equal_or(
            self.status,
            RideStatusEnum.SCHEDULED,
            self.status,
            RideStatusEnum.DELAYED,
            exc_message="Only scheduled or delayed ride can become departed",
        )
        self.status = RideStatusEnum.DEPARTED
        self.departure_time = datetime.utcnow()

        self.apply(
            events.TrainDepartedEvent(
                train_id=self.train_id,
                ride_id=self.identity,
                departure_time=self.departure_time,
            )
        )

    @singledispatchmethod
    def mutate_when(self, event: DomainEvent) -> None:
        ...

from scheduler.domain.common.identity import Identity
from scheduler.domain.schedule.commands import ReportDelayCommand
from scheduler.domain.schedule.delay_report import DelayReport
from scheduler.domain.schedule.enums import UserRoleEnum
from scheduler.domain.schedule.ride import Ride


def test_report_delay(scheduled_ride: Ride) -> None:
    command = ReportDelayCommand(
        reporter_role=UserRoleEnum.MODERATOR,
        reporter_id=Identity(),
        report_id=Identity(),
        ride_id=scheduled_ride.identity,
        comment="comment",
        delay_minutes=15,
    )

    scheduled_ride.handle(command)

    assert len(scheduled_ride.reports)
    delay_report = scheduled_ride.reports.pop()

    assert isinstance(delay_report, DelayReport)
    assert delay_report.comment == command.comment
    assert delay_report.identity == command.report_id
    assert delay_report.ride_id == command.ride_id
    assert delay_report.reporter_id == command.reporter_id

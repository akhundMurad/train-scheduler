from datetime import timedelta

from scheduler.domain.common.identity import Identity
from scheduler.domain.schedule.commands import ApproveDelayCommand, ReportDelayCommand
from scheduler.domain.schedule.enums import (
    DelayReportStatusEnum,
    RideStatusEnum,
    UserRoleEnum,
)
from scheduler.domain.schedule.ride import Ride


def test_approve_delay(scheduled_ride: Ride) -> None:
    previous_arriving_time = scheduled_ride.arriving_time
    report_delay_command = ReportDelayCommand(
        reporter_role=UserRoleEnum.MODERATOR,
        reporter_id=Identity(),
        report_id=Identity(),
        ride_id=scheduled_ride.identity,
        comment="comment",
        delay_minutes=15,
    )

    scheduled_ride.handle(report_delay_command)

    approve_delay_command = ApproveDelayCommand(
        current_user_role=UserRoleEnum.ADMIN, delay_id=report_delay_command.report_id
    )

    scheduled_ride.handle(approve_delay_command)

    assert scheduled_ride.reports[0].status == DelayReportStatusEnum.APPROVED
    assert scheduled_ride.status == RideStatusEnum.DELAYED
    assert scheduled_ride.arriving_time - previous_arriving_time == timedelta(
        minutes=15
    )

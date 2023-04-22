import pytest

from scheduler.domain.errors import DomainException
from scheduler.domain.schedule.commands.dispatch_train_command import (
    DispatchTrainCommand,
)
from scheduler.domain.schedule.enums import RideStatusEnum, UserRoleEnum
from scheduler.domain.schedule.ride import Ride


def test_dispatch_train(scheduled_ride: Ride) -> None:
    dispatch_train_command = DispatchTrainCommand(
        current_user_role=UserRoleEnum.ADMIN, ride_id=scheduled_ride.identity
    )

    scheduled_ride.handle(dispatch_train_command)

    assert scheduled_ride.status == RideStatusEnum.DEPARTED


def test_dispatch_arrived_train(arrived_ride: Ride) -> None:
    dispatch_train_command = DispatchTrainCommand(
        current_user_role=UserRoleEnum.ADMIN, ride_id=arrived_ride.identity
    )

    try:
        arrived_ride.handle(dispatch_train_command)
        pytest.fail("DomainException is expected.")
    except DomainException:
        pass

import pytest

from scheduler.domain.common.identity import Identity
from scheduler.domain.errors import DomainException
from scheduler.domain.schedule.commands import UpdateRideStatusCommand
from scheduler.domain.schedule.enums import RideStatusEnum, UserRoleEnum
from scheduler.domain.schedule.ride import Ride


def test_update_ride_status_to_scheduled(arrived_ride: Ride) -> None:
    command = UpdateRideStatusCommand(
        current_user_role=UserRoleEnum.MODERATOR,
        train_id=Identity(),
        ride_id=Identity(),
        new_status=RideStatusEnum.SCHEDULED,
    )

    arrived_ride.handle(command)

    assert arrived_ride.status == RideStatusEnum.SCHEDULED


def test_update_ride_status_to_departed(arrived_ride: Ride) -> None:
    command = UpdateRideStatusCommand(
        current_user_role=UserRoleEnum.MODERATOR,
        train_id=Identity(),
        ride_id=Identity(),
        new_status=RideStatusEnum.DEPARTED,
    )

    try:
        arrived_ride.handle(command)
        pytest.fail("DomainException is expected.")
    except DomainException:
        pass

    assert arrived_ride.status == RideStatusEnum.ARRIVED

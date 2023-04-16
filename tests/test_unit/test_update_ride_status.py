import pytest

from scheduler.domain.errors import DomainException
from scheduler.domain.schedule.entities import Ride
from scheduler.domain.schedule.enums import RideStatusEnum
from scheduler.domain.schedule.services import update_ride_status


def test_update_ride_status_to_scheduled(arrived_ride: Ride) -> None:
    update_ride_status(ride=arrived_ride, new_status=RideStatusEnum.SCHEDULED)

    assert arrived_ride.status == RideStatusEnum.SCHEDULED


def test_update_ride_status_to_departed(arrived_ride: Ride) -> None:
    try:
        update_ride_status(ride=arrived_ride, new_status=RideStatusEnum.DEPARTED)
        pytest.fail("DomainException is expected.")
    except DomainException:
        pass

    assert arrived_ride.status == RideStatusEnum.ARRIVED

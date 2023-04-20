from datetime import datetime

import pytest

from scheduler.domain.common.identity import Identity
from scheduler.domain.errors import DomainException
from scheduler.domain.schedule.ride import Ride
from scheduler.domain.schedule.train import Train
from scheduler.domain.schedule.enums import RideStatusEnum
from scheduler.domain.schedule.services import schedule_ride


def test_schedule_ride(cargo_train: Train) -> None:
    ride_data = {
        "ride_id": Identity(),
        "train_id": cargo_train.identity,
        "departure_time": datetime(2023, 8, 17),
        "arriving_time": datetime(2023, 8, 18),
        "start_station": "START",
        "end_station": "END",
    }

    ride = schedule_ride(**ride_data)

    assert isinstance(ride, Ride)
    assert ride.identity == ride_data["ride_id"]
    assert ride.train_id == cargo_train.identity
    assert ride.departure_time == ride_data["departure_time"]
    assert ride.arriving_time == ride_data["arriving_time"]
    assert ride.start_station == ride_data["start_station"]
    assert ride.end_station == ride_data["end_station"]
    assert ride.status == RideStatusEnum.SCHEDULED


def test_schedule_ride_wrong_time(cargo_train: Train) -> None:
    ride_data = {
        "ride_id": Identity(),
        "train_id": cargo_train.identity,
        "departure_time": datetime(2023, 8, 17),
        "arriving_time": datetime(2023, 8, 19),
        "start_station": "START",
        "end_station": "END",
    }

    try:
        schedule_ride(**ride_data)
        pytest.fail("DomainException is expected.")
    except DomainException:
        pass

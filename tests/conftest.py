from datetime import datetime

import pytest

from scheduler.domain.schedule.entities import Ride, Train
from scheduler.domain.schedule.enums import RideStatusEnum, TrainTypeEnum


@pytest.fixture
def cargo_train() -> Train:
    return Train(
        model="WWW",
        train_type=TrainTypeEnum.CARGO,
        wagon_seats_quantity=10,
        wagons_quantity=10,
    )


@pytest.fixture
def arrived_ride(cargo_train: Train) -> Ride:
    return Ride(
        train_id=cargo_train.identity,
        departure_time=datetime(2022, 8, 7),
        arriving_time=datetime(2022, 8, 8),
        start_station="A",
        end_station="B",
        status=RideStatusEnum.ARRIVED,
    )

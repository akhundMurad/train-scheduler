import pytest

from scheduler.domain.schedule.entities import Train
from scheduler.domain.schedule.enums import TrainTypeEnum


@pytest.fixture
def cargo_train() -> Train:
    return Train(
        model="WWW",
        train_type=TrainTypeEnum.CARGO,
        wagon_seats_quantity=10,
        wagons_quantity=10,
    )

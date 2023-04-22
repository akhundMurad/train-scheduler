from datetime import datetime

import pytest

from scheduler.domain.errors import DomainException
from scheduler.domain.schedule.ride import Ride
from scheduler.domain.schedule.train import Train


def test_schedule_ride_wrong_time(cargo_train: Train) -> None:
    try:
        _ = Ride(
            train_id=cargo_train.identity,
            departure_time=datetime(2023, 8, 17),
            arriving_time=datetime(2023, 8, 19),
            start_station="START",
            end_station="END",
        )
        pytest.fail("DomainException is expected.")
    except DomainException:
        pass

from dataclasses import dataclass, field
from datetime import datetime

from scheduler.domain.common.entity import Entity
from scheduler.domain.common.identity import Identity
from scheduler.domain.schedule.enums import RideStatusEnum, TrainTypeEnum


@dataclass(kw_only=True, eq=False)
class Train(Entity):
    model: str
    train_type: TrainTypeEnum
    wagons_quantity: int
    wagon_seats_quantity: int


class Ride(Entity):
    train_id: Identity
    departure_time: datetime
    arriving_time: datetime
    start_station: str
    end_station: str
    status: RideStatusEnum = field(default=RideStatusEnum.SCHEDULED)


class DelayReport(Entity):
    reporter_id: Identity
    ride_id: Identity
    comment: str | None = field(default=None)

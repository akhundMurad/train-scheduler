from dataclasses import dataclass, field
from datetime import datetime

from scheduler.domain.common.entity import Entity
from scheduler.domain.common.identity import Identity
from scheduler.domain.schedule.enums import RideStatusEnum


@dataclass(kw_only=True, eq=False)
class Ride(Entity):
    train_id: Identity
    departure_time: datetime
    arriving_time: datetime
    start_station: str
    end_station: str
    status: RideStatusEnum = field(default=RideStatusEnum.SCHEDULED)

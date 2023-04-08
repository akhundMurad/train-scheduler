from dataclasses import dataclass
from datetime import datetime

from diator.events import DomainEvent

from scheduler.domain.common.identity import Identity


@dataclass(frozen=True, kw_only=True)
class TrainDepartedEvent(DomainEvent):
    train_id: Identity
    ride_id: Identity
    departure_time: datetime

from dataclasses import dataclass

from diator.events import DomainEvent

from scheduler.domain.common.identity import Identity


@dataclass(frozen=True, kw_only=True)
class TrainArrivedEvent(DomainEvent):
    train_id: Identity
    ride_id: Identity

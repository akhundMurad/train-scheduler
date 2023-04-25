from dataclasses import dataclass

from diator.events import DomainEvent

from scheduler.domain.common.identity import Identity


@dataclass(frozen=True, kw_only=True)
class RideScheduledEvent(DomainEvent):
    ride_id: Identity
    train_id: Identity

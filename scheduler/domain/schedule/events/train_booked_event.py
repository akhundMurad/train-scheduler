from dataclasses import dataclass

from diator.events import DomainEvent

from scheduler.domain.common.identity import Identity


@dataclass(frozen=True, kw_only=True)
class TrainBookedEvent(DomainEvent):
    person_id: Identity
    train_id: Identity
    ride_id: Identity
    wagon_number: int
    seat_number: int

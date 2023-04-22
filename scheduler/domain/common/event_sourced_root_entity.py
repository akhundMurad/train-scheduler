from dataclasses import dataclass, field
from functools import singledispatchmethod

from diator.events import DomainEvent
from diator.requests import Request

from scheduler.domain.common.concurrency_safe_entity import ConcurrencySafeEntity


@dataclass(kw_only=True, eq=False)
class EventSourcedRootEntity(ConcurrencySafeEntity):
    _mutating_events: list[DomainEvent] = field(default_factory=list)

    @singledispatchmethod
    def handle(self, command: Request) -> None:
        ...

    @singledispatchmethod
    def when(self, event: DomainEvent) -> None:
        ...

    @property
    def mutating_events(self) -> list[DomainEvent]:
        return self._mutating_events

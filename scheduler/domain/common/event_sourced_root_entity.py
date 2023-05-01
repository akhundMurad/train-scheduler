from dataclasses import dataclass, field
from functools import singledispatchmethod

from diator.events import DomainEvent
from diator.requests import Request

from scheduler.domain.common.concurrency_safe_entity import ConcurrencySafeEntity


@dataclass(kw_only=True, eq=False)
class EventSourcedRootEntity(ConcurrencySafeEntity):
    _unmutated_version: int = field(default=0, init=False)
    _mutating_events: list[DomainEvent] = field(default_factory=list, init=False)

    @singledispatchmethod
    def handle(self, command: Request) -> None:
        ...

    @singledispatchmethod
    def when(self, event: DomainEvent) -> None:
        ...

    def apply(self, event: DomainEvent) -> None:
        self._mutating_events.append(event)
        self.when(event)

    @property
    def mutating_events(self) -> list[DomainEvent]:
        return self._mutating_events

    @property
    def mutated_version(self) -> int:
        return self._unmutated_version + 1

    def set_event_stream(
        self, event_stream: list[DomainEvent], stream_version: int
    ) -> None:
        self._mutating_events = event_stream

        for event in self._mutating_events:
            self.apply(event)

        self._unmutated_version = stream_version

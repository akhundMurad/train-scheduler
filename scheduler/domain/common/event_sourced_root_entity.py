from dataclasses import dataclass
from functools import singledispatchmethod
from diator.requests import Request
from diator.events import DomainEvent

from scheduler.domain.common.concurrency_safe_entity import ConcurrencySafeEntity


@dataclass(kw_only=True, eq=False)
class EventSourcedRootEntity(ConcurrencySafeEntity):
    @singledispatchmethod
    def handle(self, command: Request) -> None:
        ...

    @singledispatchmethod
    def when(self, event: DomainEvent) -> None:
        ...

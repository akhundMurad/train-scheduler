from dataclasses import dataclass

from diator.events import DomainEvent

from scheduler.domain.common.identity import Identity


@dataclass(frozen=True, kw_only=True)
class DelayReportedEvent(DomainEvent):
    reporter_id: Identity
    report_id: Identity
    ride_id: Identity
    delay_minutes: int

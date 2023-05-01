from dataclasses import dataclass

from diator.events import DomainEvent

from scheduler.domain.common.identity import Identity
from scheduler.domain.schedule.delay_report import DelayReport


@dataclass(frozen=True, kw_only=True)
class DelayApprovedEvent(DomainEvent):
    report_id: Identity
    ride_id: Identity
    selected_report: DelayReport
    delay_minutes: int

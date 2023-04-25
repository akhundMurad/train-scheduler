from dataclasses import dataclass

from diator.events import DomainEvent

from scheduler.domain.common.identity import Identity
from scheduler.domain.schedule.enums import RideStatusEnum


@dataclass(frozen=True, kw_only=True)
class RideStatusChangedEvent(DomainEvent):
    ride_id: Identity
    previous_status: RideStatusEnum
    new_status: RideStatusEnum

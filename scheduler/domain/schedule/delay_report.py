
from dataclasses import dataclass, field

from scheduler.domain.common.entity import Entity
from scheduler.domain.common.identity import Identity


@dataclass(kw_only=True, eq=False)
class DelayReport(Entity):
    reporter_id: Identity
    ride_id: Identity
    comment: str | None = field(default=None)

from dataclasses import dataclass, field

from scheduler.domain.common.assertion_concern import AssertionConcern
from scheduler.domain.common.identity import Identity


@dataclass(kw_only=True, eq=False)
class IdentifiedDomainObject(AssertionConcern):
    identity: Identity = field(default_factory=Identity)

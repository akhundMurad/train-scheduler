from dataclasses import dataclass, field

from scheduler.domain.common.identity import Identity


@dataclass(kw_only=True, eq=False)
class IdentifiedDomainObject:
    identity: Identity = field(default_factory=Identity)

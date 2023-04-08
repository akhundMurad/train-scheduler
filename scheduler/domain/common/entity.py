from dataclasses import dataclass, field

from scheduler.domain.common.identity import Identity


@dataclass(kw_only=True, eq=False)
class Entity:
    identity: Identity = field(default_factory=Identity)

    def __eq__(self, entity: "Entity") -> bool:
        if not isinstance(entity, Entity):
            return False
        return entity.identity == self.identity

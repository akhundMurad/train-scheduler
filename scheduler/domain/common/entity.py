from dataclasses import dataclass

from scheduler.domain.common.identified_domain_object import IdentifiedDomainObject


@dataclass(kw_only=True, eq=False)
class Entity(IdentifiedDomainObject):
    def __eq__(self, entity: "Entity") -> bool:
        if not isinstance(entity, Entity):
            return False
        return entity.identity == self.identity

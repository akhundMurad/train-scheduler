from dataclasses import dataclass

from scheduler.domain.common.assertion_concern import AssertionConcern


@dataclass(kw_only=True, frozen=True)
class IdentifiedValueObject(AssertionConcern):
    ...

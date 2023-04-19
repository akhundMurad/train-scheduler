from dataclasses import dataclass, field

from scheduler.domain.common.entity import Entity
from scheduler.domain.errors import ConcurrencyException


@dataclass(kw_only=True, eq=False)
class ConcurrencySafeEntity(Entity):
    _concurrency_version: int = field(default=0, init=True)

    @property
    def concurrency_version(self) -> int:
        return self._concurrency_version

    def set_concurrency_version(self, version: int) -> None:
        self.check_concurrency_vialation(version)
        self._concurrency_version = version

    def check_concurrency_vialation(self, version: int) -> None:
        if version != self._concurrency_version:
            raise ConcurrencyException("Entity already has been modified.")

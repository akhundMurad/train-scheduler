from typing import Callable
from uuid import UUID, uuid4

from scheduler.domain.common.identity.protocol import IdentityProtocol


class UUIDIdentity(IdentityProtocol[UUID]):
    def __init__(self, value: UUID | None = None) -> None:
        self._value = value or self.value_generator()

    @property
    def value_generator(self) -> Callable[[], UUID]:
        return uuid4

    @classmethod
    def from_string(cls, plain_str: str) -> "UUIDIdentity":
        return cls(value=UUID(plain_str))

    def __eq__(self, identity: "UUIDIdentity") -> bool:
        if not isinstance(identity, UUIDIdentity):
            return False
        return identity._value == self._value

    def __str__(self) -> str:
        return str(self._value)

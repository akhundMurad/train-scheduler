from typing import Callable, Protocol, TypeVar

IdentityType = TypeVar("IdentityType", covariant=True)


class IdentityProtocol(Protocol[IdentityType]):
    @property
    def value_generator(self) -> Callable[[], IdentityType]:
        ...

    @classmethod
    def from_string(cls, plain_str: str) -> "IdentityProtocol":
        ...

    def __eq__(self, identity: "IdentityProtocol") -> bool:
        ...

    def __str__(self) -> str:
        ...

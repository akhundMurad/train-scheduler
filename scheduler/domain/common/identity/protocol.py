from typing import Callable, Protocol, TypeVar

I = TypeVar("I")


class IdentityProtocol(Protocol[I]):
    @property
    def value_generator(self) -> Callable[[], I]:
        ...

    @classmethod
    def from_string(cls, plain_str: str) -> "IdentityProtocol":
        ...

    def __eq__(self, another_id: I) -> bool:
        ...

    def __str__(self) -> str:
        ...

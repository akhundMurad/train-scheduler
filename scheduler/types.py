from typing import Protocol, TypeVar, runtime_checkable

T_contra = TypeVar("T_contra", contravariant=True)


@runtime_checkable
class SupportsNe(Protocol[T_contra]):
    def __ne__(self, other: T_contra) -> bool:
        ...


@runtime_checkable
class SupportsGe(Protocol[T_contra]):
    def __ge__(self, other: T_contra) -> bool:
        ...

from typing import Any, Iterable

from scheduler.domain.errors import AssertionConcernException
from scheduler.types import SupportsGe


class AssertionConcern:
    def assert_is_not_none(self, value: Any, exc_message: str) -> None:
        if value is None:
            raise AssertionConcernException(exc_message)

    def assert_values_equal_or(self, *pairs, exc_message: str) -> None:
        if not any(value == to_value for (value, to_value) in pairwise(pairs)):
            raise AssertionConcernException(exc_message)

    def assert_values_equal_and(self, *pairs, exc_message: str) -> None:
        if all(value == to_value for (value, to_value) in pairwise(pairs)):
            raise AssertionConcernException(exc_message)

    def assert_value_lt(
        self, value: SupportsGe, than_value: SupportsGe, exc_message: str
    ) -> None:
        if value >= than_value:
            raise AssertionConcernException(exc_message)


def pairwise(iterable: Iterable) -> zip:
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    inner = iter(iterable)
    return zip(inner, inner)

import pytest

from scheduler.domain.common.concurrency_safe_entity import ConcurrencySafeEntity
from scheduler.domain.errors import ConcurrencyException


def test_concurrency_safe_entity() -> None:
    entity = ConcurrencySafeEntity()

    with pytest.raises(ConcurrencyException):
        entity.set_concurrency_version(1)

    try:
        entity.set_concurrency_version(0)
    except ConcurrencyException as exc:
        pytest.fail(str(exc))

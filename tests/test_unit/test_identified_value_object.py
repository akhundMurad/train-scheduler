from dataclasses import dataclass

from scheduler.domain.common.identified_value_object import IdentifiedValueObject


@dataclass(kw_only=True, frozen=True)
class Name(IdentifiedValueObject):
    name: str


def test_identified_value_object() -> None:
    name_murad = Name(name="Murad")
    name_murad_dublicate = Name(name="Murad")
    name_kamran = Name(name="Kamran")

    assert name_murad != name_kamran
    assert name_murad == name_murad_dublicate

from dataclasses import dataclass
from scheduler.domain.common.identified_value_object import IdentifiedValueObject


@dataclass(kw_only=True, frozen=True)
class TrainModel(IdentifiedValueObject):
    model_name: str
    manufacture_year: int

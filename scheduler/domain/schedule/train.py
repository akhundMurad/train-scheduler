from dataclasses import dataclass

from scheduler.domain.common.entity import Entity
from scheduler.domain.schedule.enums import TrainTypeEnum
from scheduler.domain.schedule.train_model import TrainModel


@dataclass(kw_only=True, eq=False)
class Train(Entity):
    model: TrainModel
    train_type: TrainTypeEnum
    wagons_quantity: int
    wagon_seats_quantity: int

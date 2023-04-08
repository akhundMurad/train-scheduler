from dataclasses import dataclass
from diator.events import Event


@dataclass(frozen=True, kw_only=True)
class TrainArrivedEvent(Event):
    ...
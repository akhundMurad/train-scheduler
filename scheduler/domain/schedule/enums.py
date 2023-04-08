from enum import StrEnum


class RideStatusEnum(StrEnum):
    SCHEDULED = "SCHEDULED"
    DEPARTED = "DEPARTED"
    ARRIVED = "ARRIVED"
    DELAYED = "DELAYED"
    CANCELLED = "CANCELLED"


class TrainTypeEnum(StrEnum):
    CARGO = "CARGO"
    PASSENGER = "PASSENGER"


class UserRoleEnum(StrEnum):
    MODERATOR = "MODERATOR"
    ADMIN = "ADMIN"

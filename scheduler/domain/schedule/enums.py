from enum import StrEnum


class TrainStatusEnum(StrEnum):
    SCHEDULED = "SCHEDULED"
    DEPARTED = "DEPARTED"
    ARRIVED = "ARRIVED"
    DELAYED = "DELAYED"
    CANCELLED = "CANCELLED"


class UserRoleEnum(StrEnum):
    MODERATOR = "MODERATOR"
    ADMIN = "ADMIN"

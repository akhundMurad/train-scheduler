from scheduler.domain.errors import DomainException
from scheduler.domain.schedule.entites import Ride
from scheduler.domain.schedule.enums import RideStatusEnum


def update_ride_status(*, ride: Ride, new_status: RideStatusEnum) -> None:
    if new_status == RideStatusEnum.DEPARTED and ride.status == RideStatusEnum.ARRIVED:
        raise DomainException(
            "Ride status cannot be changed to 'departed' after it was equal to 'arrived'."
        )

    ride.status = new_status

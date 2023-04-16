from datetime import datetime

from scheduler.domain.common.identity import Identity
from scheduler.domain.errors import DomainException
from scheduler.domain.schedule.constants import MAX_RIDE_PERIOD
from scheduler.domain.schedule.entities import DelayReport, Ride
from scheduler.domain.schedule.enums import RideStatusEnum


def update_ride_status(*, ride: Ride, new_status: RideStatusEnum) -> None:
    if new_status == RideStatusEnum.DEPARTED and ride.status == RideStatusEnum.ARRIVED:
        raise DomainException(
            "Ride status cannot be changed to 'departed' after it was equal to 'arrived'."
        )

    ride.status = new_status


def schedule_ride(
    *,
    ride_id: Identity,
    train_id: Identity,
    departure_time: datetime,
    arriving_time: datetime,
    start_station: str,
    end_station: str,
) -> Ride:
    period = arriving_time - departure_time
    if period >= MAX_RIDE_PERIOD:
        raise DomainException(
            f"Ride period cannot be equal or greater than {MAX_RIDE_PERIOD}"
        )

    return Ride(
        identity=ride_id,
        train_id=train_id,
        departure_time=departure_time,
        arriving_time=arriving_time,
        start_station=start_station,
        end_station=end_station,
        status=RideStatusEnum.SCHEDULED,
    )


def report_delay(
    *,
    reporter_id: Identity,
    report_id: Identity,
    ride_id: Identity,
    comment: str | None = None,
) -> DelayReport:
    return DelayReport(
        identity=report_id, reporter_id=reporter_id, ride_id=ride_id, comment=comment
    )

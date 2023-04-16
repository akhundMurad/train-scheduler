from scheduler.domain.common.identity import Identity
from scheduler.domain.schedule.entities import DelayReport, Ride
from scheduler.domain.schedule.services import report_delay


def test_report_delay(arrived_ride: Ride) -> None:
    report_data = {
        "reporter_id": Identity(),
        "report_id": Identity(),
        "ride_id": arrived_ride.identity,
        "comment": "comment",
    }

    delay_report = report_delay(**report_data)

    assert isinstance(delay_report, DelayReport)
    assert delay_report.comment == report_data["comment"]
    assert delay_report.identity == report_data["report_id"]
    assert delay_report.ride_id == arrived_ride.identity
    assert delay_report.reporter_id == report_data["reporter_id"]

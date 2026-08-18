from dataclasses import dataclass


@dataclass(frozen=True)
class TransitConditions:
    """Factors that scale raw transit time for a shipment."""

    distance: float
    traffic_factor: float
    weather_factor: float


@dataclass(frozen=True)
class DeliveryDelays:
    """Additive delays that extend the delivery window."""

    handling_hours: float
    warehouse_delay: float
    customs_delay: float
    weekend_delay: float


def delivery_window(
    conditions: TransitConditions,
    delays: DeliveryDelays,
    priority_credit: float,
) -> float:
    """Estimate a delivery window for the required-review E2E fixture."""
    transit_hours = (
        conditions.distance * conditions.traffic_factor * conditions.weather_factor
    )
    total_delays = (
        delays.handling_hours
        + delays.warehouse_delay
        + delays.customs_delay
        + delays.weekend_delay
    )
    return round(transit_hours + total_delays - priority_credit, 2)

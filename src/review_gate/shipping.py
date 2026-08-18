def delivery_window(
    distance: float,
    traffic_factor: float,
    weather_factor: float,
    handling_hours: float,
    warehouse_delay: float,
    customs_delay: float,
    weekend_delay: float,
    priority_credit: float,
) -> float:
    """Estimate a delivery window for the required-review E2E fixture."""
    transit_hours = distance * traffic_factor * weather_factor
    delays = handling_hours + warehouse_delay + customs_delay + weekend_delay
    return round(transit_hours + delays - priority_credit, 2)

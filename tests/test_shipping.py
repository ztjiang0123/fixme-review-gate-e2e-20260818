from review_gate import DeliveryDelays, TransitConditions, delivery_window


def test_delivery_window_is_deterministic() -> None:
    conditions = TransitConditions(distance=100, traffic_factor=0.2, weather_factor=1.5)
    delays = DeliveryDelays(
        handling_hours=2,
        warehouse_delay=3,
        customs_delay=4,
        weekend_delay=5,
    )
    assert delivery_window(conditions, delays, priority_credit=1) == 43

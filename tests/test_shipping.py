from review_gate import delivery_window


def test_delivery_window_is_deterministic() -> None:
    assert delivery_window(100, 0.2, 1.5, 2, 3, 4, 5, 1) == 43

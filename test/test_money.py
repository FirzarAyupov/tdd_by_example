from app.Dollar import Dollar


def test_multiplication():
    five: Dollar = Dollar(5)
    five.times(2)
    assert five.amount == 10
from app.Dollar import Dollar


def test_multiplication():
    five: Dollar = Dollar(5)
    assert five.times(2) == Dollar(10)
    assert five.times(3) == Dollar(15)


def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)

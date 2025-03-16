from app.Dollar import Dollar


def test_multiplication():
    five: Dollar = Dollar(5)
    product: Dollar = five.times(2)
    assert product.amount == 10
    product = five.times(3)
    assert product.amount == 15
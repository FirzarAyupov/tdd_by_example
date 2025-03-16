from app.Dollar import Dollar


def test_multiplication():
    five: Dollar = Dollar(5)
    product: Dollar = five.times(2)
    assert product.amount == 10
    product = five.times(3)
    assert product.amount == 15

def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)
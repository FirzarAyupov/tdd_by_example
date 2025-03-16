class Dollar:

    def __init__(self, amount: int):
        self.__amount = amount

    def times(self, multiplier: int):
        return Dollar(self.__amount * multiplier)

    def __eq__(self, other):
        if not isinstance(other, Dollar):
            return False
        return self.__amount == other.__amount

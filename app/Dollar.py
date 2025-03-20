from app.Money import Money


class Dollar(Money):

    def times(self, multiplier: int):
        return Dollar(self._amount * multiplier)

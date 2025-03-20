from app.Money import Money


class Franc(Money):

    def times(self, multiplier: int):
        return Franc(self._amount * multiplier)

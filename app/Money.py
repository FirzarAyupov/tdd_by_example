class Money:

    def __init__(self, amount: int):
        self._amount = amount

    def __eq__(self, other: object):
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount

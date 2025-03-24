class Money:

    def __init__(self, amount: int):
        self._amount = amount

    def __eq__(self, other: object):
        return (isinstance(other, self.__class__)
                and self._amount == other._amount)

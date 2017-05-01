from decimal import Decimal


class Fees(object):
    def __init__(self):
        """constructor"""
        self._fee = None

    def get_fee(self):
        """return the current fee"""
        return self._fee

    def set_fee(self, value):
        """set the fee"""
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value

    fee = property(get_fee, set_fee)

f = Fees()
f.set_fee("1")
print(f.fee)
print(f.get_fee())
f.fee = "2"
print(f.get_fee())
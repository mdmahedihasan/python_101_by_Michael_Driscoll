from decimal import Decimal


class Fees(object):
    def __init__(self):
        """constructor"""
        self._fee = None


    @property
    def fee(self):
        """the fee property - the getter"""
        return self._fee

    @fee.setter
    def fee(self, value):
        """the setter of the fee property"""
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value

if __name__ == '__main__':
    f = Fees()
import sys


class CarClass:
    """"""
    def __init__(self, color, make, model, year):
        """"""
        self.color = color
        self.make = make
        self.model = model
        self.year = year

        if "Linux" in platform.platform():
            print("you are using linux")

        self.weight = self.getWeight(1, 2, 3)

    def getWeight(this):
        """"""
        return "2000 lbs"
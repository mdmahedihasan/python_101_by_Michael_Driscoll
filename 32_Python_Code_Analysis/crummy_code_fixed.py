import platform


class CarClass():
    """"""
    def __init__(self, color, make, model, year):
        """"""
        self.color = color
        self.make = make
        self.model = model
        self.year = year

        if "Linux" in platform.platform():
            print("You are using linux")

        self.weight = self.get_weight(3)

    def get_weight(self, this):
        """"""
        return "2000 lbs"
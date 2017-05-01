import unittest


class TestBowling(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_all_ones(self):
        pins = [1 for i in range(11)]
        self.game.roll(11, pins)
        self.assertEqual(self.game.score, 11)

    def test_spare(self):
        self.game.roll(11, [5, 5, 5, 4])
        self.assertEqual(self.game.score, 24)

    def test_strike(self):
        self.game.roll(11, [10, 5, 4])
        self.assertEqual(self.game.score, 28)


class Game():
    def __init__(self):
        self.score = 0
        self.pins = [0 for i in range(11)]

    def roll(self, numberOfRolls, pins):
        x = 0
        for pin in pins:
            self.pins[x] = pin
            x += 1
        x = 0
        spare_begin = 0
        spare_end = 2
        for roll in range(numberOfRolls):
            spare = sum(self.pins[spare_begin:spare_end])
            if self.pins[x] == 10:
                self.score = self.pins[x] + self.pins[x + 1] + self.pins[x + 2]
            elif spare == 10:
                self.score = spare + self.pins[x + 2]
                x += 1
            else:
                self.score += self.pins[x]
            x += 1
            if x == 11:
                break
            spare_begin += 2
            spare_end += 2
        print(self.score)


if __name__ == '__main__':
    unittest.main()
import unittest


class TestBowling(unittest.TestCase):
    def test_all_ones(self):
        """constructor"""
        game = Game()
        game.roll(11, 1)
        self.assertEqual(game.score, 11)


class Game():
    def __init__(self):
        """constructor"""
        self.score = 0

    def roll(self, numOfRolls, pins):
        for roll in range(numOfRolls):
            self.score += pins


if __name__ == '__main__':
    unittest.main()
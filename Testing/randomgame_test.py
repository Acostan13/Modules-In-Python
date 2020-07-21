import unittest
from Testing import randomgame


class TestMain(unittest.TestCase):
    def setUp(self):
        print('let the testing begin')

    def test_right_guess(self):
        guess = 5
        answer = 5
        result = randomgame.lets_play(guess, answer)
        self.assertTrue(result)  # OK

    def test_wrong_guess(self):
        result = randomgame.lets_play(5, 0)
        self.assertFalse(result)  # OK

    def test_wrong_number(self):
        result = randomgame.lets_play(5, 11)
        self.assertFalse(result)  # OK

    def test_wrong_type(self):
        result = randomgame.lets_play(5, 'string')
        self.assertFalse(result)  # TypeError: '>=' not supported between instances of 'int' and 'str'


if __name__ == '__main__':
    unittest.main()

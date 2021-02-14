import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.tournament_winner import Solution


class Test(unittest.TestCase):
    def test_winner(self):
        self.assertEqual(
            Solution().winner(
                [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]], [0, 0, 1]
            ),
            "Python",
        )


if __name__ == "__main__":
    unittest.main()

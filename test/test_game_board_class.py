import unittest

import sys

from chess.game_board import GameBoard
from chess.empty_space import Empty_Space


class TestGameBoard(unittest.TestCase):
    def test_empty_instance(self):
        game_board = GameBoard()
        self.assertIsInstance(game_board.pieces[0][0], Empty_Space)


if __name__ == "__main__":
    unittest.main()


# assertEqual(a, b)         a == b
# assertNotEqual(a, b)      a != b
# assertTrue(x)             bool(x) is True
# assertFalse(x)            bool(x) is False
# assertIs(a, b)            a is b
# assertIsNot(a, b)         a is not b
# assertIsNone(x)           x is None
# assertIsNotNone(x)        x is not None
# assertIn(a, b)            a in b
# assertNotIn(a, b)         a not in b
# assertIsInstance(a, b)    isinstance(a, b)
# assertNotIsInstance(a, b) isinstance(a, b)

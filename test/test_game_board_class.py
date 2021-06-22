import unittest

from chess.gameboard.game_board import GameBoard
from chess.gameboard.empty_space import Empty_Space
from chess.gameboard.square import Square


class TestGameBoard(unittest.TestCase):
    def test_empty_instance(self):
        game_board = GameBoard()
        # Test game_board __init__ method
        self.assertEqual(game_board.cols, "ABCDEFGH")
        self.assertIsNotNone(game_board.pieces)

    def test_game_board_board_array_empty_instance(self):
        game_board = GameBoard()
        # Test that game_board.board is a 8 X 8 Array
        self.assertEqual(len(game_board.board), 8)
        self.assertEqual(len(game_board.board[0]), 8)
        self.assertEqual(len(game_board.board[1]), 8)
        self.assertEqual(len(game_board.board[2]), 8)
        self.assertEqual(len(game_board.board[3]), 8)
        self.assertEqual(len(game_board.board[4]), 8)
        self.assertEqual(len(game_board.board[5]), 8)
        self.assertEqual(len(game_board.board[6]), 8)
        self.assertEqual(len(game_board.board[7]), 8)

    def test_squares_in_empty_instance(self):
        # Test that the board is populated with instances of Square
        game_board = GameBoard()
        for row in range(8):
            for col in range(8):
                self.assertIsInstance(game_board.board[row][col], Square)

    def test_squares_have_correct_labels_empty_instance(self):
        # Test the square labeles
        game_board = GameBoard()
        for row in range(8):
            for col in range(8):
                correct_row_label = 8 - row
                correct_col_label = "ABCDEFGH"[col]
                board_square = game_board.board[row][col]
                self.assertEqual(
                    board_square.cornor_label, f"{correct_col_label}{correct_row_label}"
                )


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

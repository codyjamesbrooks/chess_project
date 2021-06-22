import unittest

# Boards imports
from chess.gameboard.game_board import GameBoard
from chess.gameboard.empty_space import Empty_Space
from chess.gameboard.square import Square

# Piece imports
from chess.pieces.rook import Rook
from chess.pieces.bishop import Bishop
from chess.pieces.king import King
from chess.pieces.knight import Knight
from chess.pieces.pawn import Pawn
from chess.pieces.queen import Queen

from test.test_boards.test_boards import test_boards

test_piece_key = {
    "R": Rook("blue"),
    "r": Rook("red"),
    "B": Bishop("blue"),
    "b": Bishop("red"),
    "N": Knight("blue"),
    "n": Knight("red"),
    "Q": Queen("blue"),
    "q": Queen("red"),
    "K": King("blue"),
    "k": King("red"),
    "P": Pawn("blue"),
    "p": Pawn("red"),
    "0": Empty_Space(),
}


def populate_test_piece_array(test_board_string):
    # function will take a test board, and generate a pieces array
    test_board_string_rows = test_board_string.split(" ")
    test_pieces = []
    for row in range(8):
        test_pieces.append([])
        for piece_letter in list(test_board_string_rows[row]):
            test_pieces[row].append(test_piece_key[piece_letter])
    return test_pieces


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
        for row in range(8):
            self.assertEqual(len(game_board.board[row]), 8)

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

    # Just blue pieces
    def test_board_0_pieces_is_the_correct_size(self):
        pieces_array = populate_test_piece_array(test_boards[0])
        game_board = GameBoard(pieces_array)
        self.assertEqual(len(game_board.pieces), 8)
        for row in range(8):
            self.assertEqual(len(game_board.pieces[row]), 8)

    def test_board_0_board_is_the_correct_size(self):
        pieces_array = populate_test_piece_array(test_boards[0])
        game_board = GameBoard(pieces_array)
        self.assertEqual(len(game_board.board), 8)
        for row in range(8):
            self.assertEqual(len(game_board.board[row]), 8)

    def test_board_0_pieces_array_correct_piece(self):
        pieces_array = populate_test_piece_array(test_boards[0])
        game_board = GameBoard(pieces_array)
        expected_class = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col in range(8):
            self.assertIsInstance(game_board.pieces[0][col], expected_class[col])
        for col in range(8):
            self.assertIsInstance(game_board.pieces[1][col], Pawn)
        for row in range(2, 8):
            for col in range(8):
                self.assertIsInstance(game_board.pieces[row][col], Empty_Space)

    def test_board_0_board_array_correct_piece(self):
        pieces_array = populate_test_piece_array(test_boards[0])
        game_board = GameBoard(pieces_array)
        expected_class = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col in range(8):
            self.assertIsInstance(game_board.board[0][col], Square)
            self.assertIsInstance(game_board.board[0][col].piece, expected_class[col])
        for col in range(8):
            self.assertIsInstance(game_board.board[1][col], Square)
            self.assertIsInstance(game_board.board[1][col].piece, Pawn)
        for row in range(2, 8):
            for col in range(8):
                self.assertIsInstance(game_board.board[row][col], Square)
                self.assertIsInstance(game_board.board[row][col].piece, Empty_Space)

    def test_board_0_board_array_piece_color(self):
        pieces_array = populate_test_piece_array(test_boards[0])
        game_board = GameBoard(pieces_array)
        for row in range(2):
            for col in range(8):
                self.assertEqual(game_board.board[row][col].piece.color, "blue")
        for row in range(2, 8):
            for col in range(8):
                self.assertIsNone(game_board.board[row][col].piece.color, None)

    # Just Red pieces
    def test_board_1_pieces_is_the_correct_size(self):
        pieces_array = populate_test_piece_array(test_boards[1])
        game_board = GameBoard(pieces_array)
        self.assertEqual(len(game_board.pieces), 8)
        for row in range(8):
            self.assertEqual(len(game_board.pieces[row]), 8)

    def test_board_1_board_is_the_correct_size(self):
        pieces_array = populate_test_piece_array(test_boards[1])
        game_board = GameBoard(pieces_array)
        self.assertEqual(len(game_board.board), 8)
        for row in range(8):
            self.assertEqual(len(game_board.board[row]), 8)

    def test_board_1_pieces_array_correct_piece(self):
        pieces_array = populate_test_piece_array(test_boards[1])
        game_board = GameBoard(pieces_array)
        expected_class = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for row in range(0, 6):
            for col in range(8):
                self.assertIsInstance(game_board.pieces[row][col], Empty_Space)
        for col in range(8):
            self.assertIsInstance(game_board.pieces[6][col], Pawn)
        for col in range(8):
            self.assertIsInstance(game_board.pieces[7][col], expected_class[col])

    def test_board_1_board_array_correct_piece(self):
        pieces_array = populate_test_piece_array(test_boards[1])
        game_board = GameBoard(pieces_array)
        expected_class = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for row in range(0, 6):
            for col in range(8):
                self.assertIsInstance(game_board.board[row][col], Square)
                self.assertIsInstance(game_board.board[row][col].piece, Empty_Space)
        for col in range(8):
            self.assertIsInstance(game_board.board[6][col], Square)
            self.assertIsInstance(game_board.board[6][col].piece, Pawn)
        for col in range(8):
            self.assertIsInstance(game_board.board[7][col], Square)
            self.assertIsInstance(game_board.board[7][col].piece, expected_class[col])

    def test_board_1_board_array_piece_color(self):
        pieces_array = populate_test_piece_array(test_boards[1])
        game_board = GameBoard(pieces_array)
        for row in range(0, 6):
            for col in range(8):
                self.assertIsNone(game_board.board[row][col].piece.color, None)
        for row in range(6, 8):
            for col in range(8):
                self.assertEqual(game_board.board[row][col].piece.color, "red")

    # Inital Setup
    def test_board_2_pieces_is_the_correct_size(self):
        pieces_array = populate_test_piece_array(test_boards[2])
        game_board = GameBoard(pieces_array)
        self.assertEqual(len(game_board.pieces), 8)
        for row in range(8):
            self.assertEqual(len(game_board.pieces[row]), 8)

    def test_board_2_board_is_the_correct_size(self):
        pieces_array = populate_test_piece_array(test_boards[2])
        game_board = GameBoard(pieces_array)
        self.assertEqual(len(game_board.board), 8)
        for row in range(8):
            self.assertEqual(len(game_board.board[row]), 8)

    def test_board_2_pieces_array_correct_piece(self):
        pieces_array = populate_test_piece_array(test_boards[2])
        game_board = GameBoard(pieces_array)
        expected_class = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for row in [0, 7]:
            for col in range(8):
                self.assertIsInstance(game_board.pieces[row][col], expected_class[col])
        for row in [1, 6]:
            for col in range(8):
                self.assertIsInstance(game_board.pieces[row][col], Pawn)
        for row in range(2, 6):
            for col in range(8):
                self.assertIsInstance(game_board.pieces[row][col], Empty_Space)

    def test_board_2_board_array_correct_piece(self):
        pieces_array = populate_test_piece_array(test_boards[2])
        game_board = GameBoard(pieces_array)
        expected_class = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for row in [0, 7]:
            for col in range(8):
                self.assertIsInstance(game_board.board[row][col], Square)
                self.assertIsInstance(
                    game_board.board[row][col].piece, expected_class[col]
                )
        for row in [1, 6]:
            for col in range(8):
                self.assertIsInstance(game_board.board[row][col], Square)
                self.assertIsInstance(game_board.board[row][col].piece, Pawn)
        for row in range(2, 6):
            for col in range(8):
                self.assertIsInstance(game_board.board[row][col], Square)
                self.assertIsInstance(game_board.board[row][col].piece, Empty_Space)

    def test_board_2_board_array_piece_color(self):
        pieces_array = populate_test_piece_array(test_boards[2])
        game_board = GameBoard(pieces_array)
        for row in range(2, 6):
            for col in range(8):
                self.assertIsNone(game_board.board[row][col].piece.color, None)
        for row in range(0, 2):
            for col in range(8):
                self.assertEqual(game_board.board[row][col].piece.color, "blue")
        for row in range(6, 8):
            for col in range(8):
                self.assertEqual(game_board.board[row][col].piece.color, "red")


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

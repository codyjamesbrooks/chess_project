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
from tests.test_resources.test_boards import test_boards
inital_setup = test_boards[0]
mvmt_board_1 = test_boards[1]

class TestGameBoard(unittest.TestCase):
    def test_init_game_board(self):
        game_board = GameBoard(inital_setup)
        self.assertEqual(game_board.columns, "ABCDEFGH")
        self.assertIsNotNone(game_board.pieces)
        self.assertEqual(game_board.pieces, inital_setup)

    def test_inital_setup_pieces_correct_size(self):
        game_board = GameBoard(inital_setup)
        self.assertEqual(len(game_board.pieces), 8)
        for row in range(8):
            self.assertEqual(len(game_board.pieces[row]), 8)

    def test_game_board_board_array_size(self): 
        game_board = GameBoard(inital_setup)
        self.assertEqual(len(game_board.board), 8)
        for row in range(8): 
            self.assertEqual(len(game_board.board[row]), 8)

    def test_game_board_board_is_all_squares(self): 
        game_board = GameBoard(inital_setup)
        for row in range(8): 
            for col in range(8):
                self.assertIsInstance(game_board.board[row][col], Square)

    def test_board_squares_have_correct_labels(self): 
        game_board = GameBoard(inital_setup)
        for row in range(8): 
            for col in range(8): 
                correct_label = f"{'ABCDEFGH'[col]}{8 - row}"
                board_square = game_board.board[row][col]
                self.assertEqual(board_square.cornor_label, correct_label)

    def test_pieces_positions_match_square_cornor_labels(self): 
        game_board = GameBoard(inital_setup)
        for row in range(8):
            for col in range(8): 
                piece = game_board.pieces[row][col]
                square = game_board.board[row][col]
                if piece != Empty_Space():
                    self.assertEqual(piece.position, square.cornor_label)
                    
    def test_inital_setup_pieces_array_correct_piece(self):
        game_board = GameBoard(inital_setup)
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

    def test_inital_setup_board_array_correct_piece(self):
        game_board = GameBoard(inital_setup)
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

    def test_inital_setup_board_array_piece_color(self):
        game_board = GameBoard(inital_setup)
        for row in range(2, 6):
            for col in range(8):
                self.assertIsNone(game_board.board[row][col].piece.color, None)
        for row in range(0, 2):
            for col in range(8):
                self.assertEqual(game_board.board[row][col].piece.color, "blue")
        for row in range(6, 8):
            for col in range(8):
                self.assertEqual(game_board.board[row][col].piece.color, "red")

    def test_inital_setup_get_piece_at_position_method(self): 
        game_board = GameBoard(inital_setup)
        expected_class = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for color, row in [("blue", 8), ("red", 1)]:
            for col in list("ABCDEFGH"):
                royal_loc = f"{col}{row}"
                col_index = "ABCDEFGH".index(col)
                self.assertEqual(game_board.get_piece_at_position(royal_loc), expected_class[col_index](color, royal_loc))
        for color, row in [("blue", 7), ("red", 2)]:
            for col in list("ABCDEFGH"):
                pawn_loc = f"{col}{row}"
                self.assertEqual(game_board.get_piece_at_position(pawn_loc), Pawn(color, pawn_loc))
        for row in range(3, 7):
            for col in list("ABCDEFGH"): 
                loc = f"{col}{row}"
                self.assertEqual(game_board.get_piece_at_position(loc), Empty_Space())
                
    def test_inital_setup_get_pieces_in_col_list(self):
        game_board = GameBoard(inital_setup)
        expect_dict = { "A": [Rook("blue", "A8"), Pawn("blue", "A7"), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Pawn("red", "A2"), Rook("red", "A1")], 
                        "B": [Knight("blue", "B8"), Pawn("blue", "B7"), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Pawn("red", "B2"), Knight("red", "B1")],
                        "C": [Bishop("blue", "C8"), Pawn("blue", "C7"), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Pawn("red", "C2"), Bishop("red", "C1")],
                        "D": [Queen("blue", "D8"), Pawn("blue", "D7"), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Pawn("red", "D2"), Queen("red", "D1")],
                        "E": [King("blue", "E8"), Pawn("blue", "E7"), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Pawn("red", "E2"), King("red", "E1")],
                        "F": [Bishop("blue", "F8"), Pawn("blue", "F7"), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Pawn("red", "F2"), Bishop("red", "F1")],
                        "G": [Knight("blue", "G8"), Pawn("blue", "G7"), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Pawn("red", "G2"), Knight("red", "G1")],
                        "H": [Rook("blue", "H8"), Pawn("blue", "H7"), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Pawn("red", "H2"), Rook("red", "H1")]}
        for col in list("ABCDEFGH"): 
            self.assertEqual(game_board.get_pieces_in_col_list(col), expect_dict[col])

    def test_inital_setup_get_pieces_in_row_list(self):
        game_board = GameBoard(inital_setup)
        expect_dict = { '8': [Rook("blue", "A8"), Knight("blue", "B8"), Bishop("blue", "C8"), Queen("blue", "D8"), King("blue", "E8"), Bishop("blue", "F8"), Knight("blue", "G8"), Rook("blue", "H8")],
                        '7': [Pawn("blue", "A7"), Pawn("blue", "B7"), Pawn("blue", "C7"), Pawn("blue", "D7"), Pawn("blue", "E7"), Pawn("blue", "F7"), Pawn("blue", "G7"), Pawn("blue", "H7")],
                        '6': [Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space()],
                        '5': [Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space()],
                        '4': [Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space()], 
                        '3': [Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space()],
                        '2': [Pawn("red", "A2"), Pawn("red", "B2"), Pawn("red", "C2"), Pawn("red", "D2"), Pawn("red", "E2"), Pawn("red", "F2"), Pawn("red", "G2"), Pawn("red", "H2")],
                        '1': [Rook("red", "A1"), Knight("red", "B1"), Bishop("red", "C1"), Queen("red", "D1"), King("red", "E1"), Bishop("red", "F1"), Knight("red", "G1"), Rook("red", "H1")]}
        for row in range(1, 9):
            self.assertEqual(game_board.get_pieces_in_row_list(str(row)), expect_dict[str(row)])

    def test_set_pieces_method(self): 
        game_board = GameBoard(inital_setup)
        game_board.set_pieces(mvmt_board_1)
        self.assertEqual(game_board.pieces, mvmt_board_1)

    

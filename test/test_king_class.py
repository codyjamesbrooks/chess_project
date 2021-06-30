import unittest
# Boards imports
from chess.gameboard.game_board import GameBoard

# Piece imports
from chess.pieces.king import King

from test.test_boards.test_boards import test_boards
inital_setup = test_boards[0]
mvmt_board_1 = test_boards[1]
mvmt_board_2 = test_boards[2]
mvmt_board_3 = test_boards[3]
mvmt_board_4 = test_boards[4]

class TestKingClass(unittest.TestCase): 
    def test_init_red_king(self): 
        king = King("red", "A8")
        self.assertEqual(king.name, "King")
        self.assertEqual(king.alias, "K")
        self.assertEqual(king.color, "red")
        self.assertEqual(king.position, "A8")
        self.assertEqual(king.current_col, "A")
        self.assertEqual(king.current_row, "8")

    def test_get_moves_on_inital_setup(self): 
        game_board = GameBoard(inital_setup)
        positions = ["E8", "E1"]
        for position in positions: 
            king = game_board.get_piece_at_position(position)
            moves = king.get_moves(game_board)
            self.assertEqual(moves["moves"], [])
            self.assertEqual(moves["captures"], [])

    def test_moves_mb1_kH8(self): 
        game_board = GameBoard(mvmt_board_1)
        king = game_board.get_piece_at_position("H8")
        moves = king.get_moves(game_board)
        self.assertEqual(moves["moves"], ["G7"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb1_kH1(self): 
        game_board = GameBoard(mvmt_board_1)
        king = game_board.get_piece_at_position("H1")
        moves = king.get_moves(game_board)
        self.assertEqual(moves["moves"], ["G1"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_kE8(self): 
        game_board = GameBoard(mvmt_board_2)
        king = game_board.get_piece_at_position("E8")
        moves = king.get_moves(game_board)
        self.assertEqual(moves["moves"], ["E7", "F7"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_kE1(self): 
        game_board = GameBoard(mvmt_board_2)
        king = game_board.get_piece_at_position("E1")
        moves = king.get_moves(game_board)
        self.assertEqual(moves["moves"], ["D2", "E2", "F2"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb3_kE8(self): 
        game_board = GameBoard(mvmt_board_3)
        king = game_board.get_piece_at_position("E8")
        moves = king.get_moves(game_board)
        self.assertEqual(moves["moves"], ["D7", "D8", "F7", "F8"])
        self.assertEqual(moves["captures"], ["E7"])

    def test_moves_mb3_kE1(self): 
        game_board = GameBoard(mvmt_board_3)
        king = game_board.get_piece_at_position("E1")
        moves = king.get_moves(game_board)
        self.assertEqual(moves["moves"], ["D2", "F2"])
        self.assertEqual(moves["captures"], ["E2"])

    def test_moves_mb4_kG8(self): 
        game_board = GameBoard(mvmt_board_4)
        king = game_board.get_piece_at_position("G8")
        moves = king.get_moves(game_board)
        self.assertEqual(moves["moves"], ["F8", "H8"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb4_kG1(self): 
        game_board = GameBoard(mvmt_board_4)
        king = game_board.get_piece_at_position("G1")
        moves = king.get_moves(game_board)
        self.assertEqual(moves["moves"], ["F1", "F2", "G2", "H1"])
        self.assertEqual(moves["captures"], [])
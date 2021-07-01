import unittest
# Boards imports
from chess.gameboard.game_board import GameBoard
# Piece imports
from chess.pieces.queen import Queen
from tests.test_resources.test_boards import test_boards
inital_setup = test_boards[0]
mvmt_board_1 = test_boards[1]
mvmt_board_2 = test_boards[2]
mvmt_board_3 = test_boards[3]
mvmt_board_4 = test_boards[4]

class TestQueenClass(unittest.TestCase): 
    def test_init_red_queen(self): 
        test_queen = Queen("red", "A8")
        self.assertEqual(test_queen.name, "Queen")
        self.assertEqual(test_queen.alias, "Q")
        self.assertEqual(test_queen.color, "red")
        self.assertEqual(test_queen.position, "A8")
        self.assertEqual(test_queen.current_col, "A")
        self.assertEqual(test_queen.current_row, "8")

    def test_get_moves_on_inital_setup(self): 
        game_board = GameBoard(inital_setup)
        positions = ["D8", "D1"]
        for position in positions: 
            queen = game_board.get_piece_at_position(position)
            moves = queen.get_moves(game_board)
            self.assertEqual(moves["moves"], [])
            self.assertEqual(moves["captures"], [])

    def test_moves_mb1_qD8(self): 
        game_board = GameBoard(mvmt_board_1)
        queen = game_board.get_piece_at_position("D8")
        moves = queen.get_moves(game_board)
        self.assertEqual(moves["moves"], ["C8", "B8", "D7", "D6", "D5", "D4", "D3", "D2", "D1", "E7"])
        self.assertEqual(moves["captures"], ["F6"])

    def test_moves_mb1_qH4(self): 
        game_board = GameBoard(mvmt_board_1)
        queen = game_board.get_piece_at_position("H4")
        moves = queen.get_moves(game_board)
        self.assertEqual(moves["moves"], ["G4", "F4", "H3", "H5", "H6", "G5", "G3", "F2", "E1"])
        self.assertEqual(moves["captures"], ["H7"])

    def test_moves_mb2_qD8(self): 
        game_board = GameBoard(mvmt_board_2)
        queen = game_board.get_piece_at_position("D8")
        moves = queen.get_moves(game_board)
        self.assertEqual(moves["moves"], ["C7", "B6", "A5", "E7", "F6", "G5", "H4"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_qD1(self): 
        game_board = GameBoard(mvmt_board_2)
        queen = game_board.get_piece_at_position("D1")
        moves = queen.get_moves(game_board)
        self.assertEqual(moves["moves"], ["D2", "C2", "E2"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb3_qE5(self): 
        game_board = GameBoard(mvmt_board_3)
        queen = game_board.get_piece_at_position("E5")
        moves = queen.get_moves(game_board)
        self.assertEqual(moves["moves"], ["D5", "C5", "B5", "A5", "E6", "D4", "C3", "F4", "G3", "H2"])
        self.assertEqual(moves["captures"], ["F5", "E4", "E7", "D6", "B2"])

    def test_moves_mb3_qD1(self): 
        game_board = GameBoard(mvmt_board_3)
        queen = game_board.get_piece_at_position("D1")
        moves = queen.get_moves(game_board)
        self.assertEqual(moves["moves"], ["D2", "D3", "D4", "D5"])
        self.assertEqual(moves["captures"], ["C2", "E2"])

    def test_moves_mb4_q(self): 
        game_board = GameBoard(mvmt_board_4)
        queen = game_board.get_piece_at_position("B2")
        moves = queen.get_moves(game_board)
        self.assertEqual(moves["moves"], ["A2", "B1", "C3", "C1"])
        self.assertEqual(moves["captures"], ["C2", "B3", "A3", "D4", "A1"])
    

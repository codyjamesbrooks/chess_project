import unittest
# Boards imports
from chess.gameboard.game_board import GameBoard

# Piece imports
from chess.pieces.knight import Knight

from tests.test_resources.test_boards import test_boards
inital_setup = test_boards[0]
mvmt_board_1 = test_boards[1]
mvmt_board_2 = test_boards[2]
mvmt_board_3 = test_boards[3]
mvmt_board_4 = test_boards[4]

class TestKnightClass(unittest.TestCase): 
    def test_init_red_knight(self): 
        test_knight = Knight("red", "A8")
        self.assertEqual(test_knight.name, "Knight")
        self.assertEqual(test_knight.alias, "N")
        self.assertEqual(test_knight.color, "red")
        self.assertEqual(test_knight.position, "A8")
        self.assertEqual(test_knight.current_col, "A")
        self.assertEqual(test_knight.current_row, "8")

    def test_get_moves_on_inital_setup(self): 
        game_board = GameBoard(inital_setup)
        blue_positions = ["B8", "G8"]
        for position in blue_positions: 
            knight = game_board.get_piece_at_position(position)
            moves = knight.get_moves(game_board)
            expect_cols = { "B": "CA", "G": "HF" }[position[0]]
            self.assertEqual(moves["moves"], [f"{expect_cols[0]}6", f"{expect_cols[1]}6"])
        red_positions = ["B1", "G1"]
        for position in red_positions: 
            knight = game_board.get_piece_at_position(position)
            moves = knight.get_moves(game_board)
            expect_cols = { "B": "AC", "G": "FH" }[position[0]]
            self.assertEqual(moves["moves"], [f"{expect_cols[0]}3", f"{expect_cols[1]}3"])

    def test_moves_mb1_nC6(self): 
        game_board = GameBoard(mvmt_board_1)
        knight = game_board.get_piece_at_position("C6")
        moves = knight.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B8", "E7", "D4"])
        self.assertEqual(moves["captures"], ["E5", "B4", "A5"])

    def test_moves_mb1_nC6(self): 
        game_board = GameBoard(mvmt_board_1)
        knight = game_board.get_piece_at_position("C6")
        moves = knight.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B8", "E7", "D4"])
        self.assertEqual(moves["captures"], ["E5", "B4", "A5"])

    def test_moves_mb1_nE5(self): 
        game_board = GameBoard(mvmt_board_1)
        knight = game_board.get_piece_at_position("E5")
        moves = knight.get_moves(game_board)
        self.assertEqual(moves["moves"], ["D7", "G4", "D3"])
        self.assertEqual(moves["captures"], ["C6", "F7", "G6"])
    
    def test_moves_mb2_nB8(self): 
        game_board = GameBoard(mvmt_board_2)
        knight = game_board.get_piece_at_position("B8")
        moves = knight.get_moves(game_board)
        self.assertEqual(moves["moves"], ["A6"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_nG8(self): 
        game_board = GameBoard(mvmt_board_2)
        knight = game_board.get_piece_at_position("G8")
        moves = knight.get_moves(game_board)
        self.assertEqual(moves["moves"], ["H6", "F6", "E7"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_nB1(self): 
        game_board = GameBoard(mvmt_board_2)
        knight = game_board.get_piece_at_position("B1")
        moves = knight.get_moves(game_board)
        self.assertEqual(moves["moves"], ["A3", "C3", "D2"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_nG1(self): 
        game_board = GameBoard(mvmt_board_2)
        knight = game_board.get_piece_at_position("G1")
        moves = knight.get_moves(game_board)
        self.assertEqual(moves["moves"], ["E2"])
        self.assertEqual(moves["captures"], ["H3"])

    def test_moves_mb3_nA7(self): 
        game_board = GameBoard(mvmt_board_3)
        knight = game_board.get_piece_at_position("A7")
        moves = knight.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B5"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb3_nF6(self): 
        game_board = GameBoard(mvmt_board_3)
        knight = game_board.get_piece_at_position("F6")
        moves = knight.get_moves(game_board)
        self.assertEqual(moves["moves"], ["D7", "G8", "G4", "D5"])
        self.assertEqual(moves["captures"], ["H7", "E4"])

    def test_moves_mb3_nF3(self): 
        game_board = GameBoard(mvmt_board_3)
        knight = game_board.get_piece_at_position("F3")
        moves = knight.get_moves(game_board)
        self.assertEqual(moves["moves"], ["D4", "G5", "H4", "H2", "G1", "D2"])
        self.assertEqual(moves["captures"], ["E5"])

    def test_moves_mb3_nB1(self): 
        game_board = GameBoard(mvmt_board_3)
        knight = game_board.get_piece_at_position("B1")
        moves = knight.get_moves(game_board)
        self.assertEqual(moves["moves"], ["C3", "D2"])
        self.assertEqual(moves["captures"], ["A3"])




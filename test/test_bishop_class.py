import unittest
# Boards imports
from chess.gameboard.game_board import GameBoard

# Piece imports
from chess.pieces.bishop import Bishop

from test.test_boards.test_boards import test_boards
inital_setup = test_boards[0]
mvmt_board_1 = test_boards[1]
mvmt_board_2 = test_boards[2]
mvmt_board_3 = test_boards[3]
mvmt_board_4 = test_boards[4]

class TestBishopClass(unittest.TestCase): 
    def test_init_red_bishop(self): 
        test_bishop = Bishop("red", "A8")
        self.assertEqual(test_bishop.name, "Bishop")
        self.assertEqual(test_bishop.alias, "B")
        self.assertEqual(test_bishop.color, "red")
        self.assertEqual(test_bishop.position, "A8")
        self.assertEqual(test_bishop.current_col, "A")
        self.assertEqual(test_bishop.current_row, "8")

    def test_get_moves_on_inital_setup(self): 
        # Every Rook in the inital setup should have no possible moves
        # and 0 possible captures. 
        game_board = GameBoard(inital_setup)
        positions = ["C8", "F8", "C1", "F1"]
        for position in positions: 
            bishop = game_board.get_piece_at_position(position)
            moves = bishop.get_moves(game_board)
            self.assertEqual(moves["moves"], [])
            self.assertEqual(moves["captures"], [])

    def test_moves_mb1_bE8(self): 
        game_board = GameBoard(mvmt_board_1)
        bishop = game_board.get_piece_at_position("E8")
        moves = bishop.get_moves(game_board)
        self.assertEqual(moves["moves"], ["D7"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb1_bC7(self): 
        game_board = GameBoard(mvmt_board_1)
        bishop = game_board.get_piece_at_position("C7")
        moves = bishop.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B8", "B6", "D6"])
        self.assertEqual(moves["captures"], ["A5", "E5"])

    def test_moves_mb1_bA5(self): 
        game_board = GameBoard(mvmt_board_1)
        bishop = game_board.get_piece_at_position("A5")
        moves = bishop.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B6"])
        self.assertEqual(moves["captures"], ["C7"])

    def test_moves_mb1_bC4(self): 
        game_board = GameBoard(mvmt_board_1)
        bishop = game_board.get_piece_at_position("C4")
        moves = bishop.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B5", "A6", "D5", "B3", "A2", "D3", "E2", "F1"])
        self.assertEqual(moves["captures"], ["E6"])

    def test_moves_mb2_bC8(self): 
        game_board = GameBoard(mvmt_board_2)
        bishop = game_board.get_piece_at_position("C8")
        moves = bishop.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B7", "A6"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_bF8(self): 
        game_board = GameBoard(mvmt_board_2)
        bishop = game_board.get_piece_at_position("F8")
        moves = bishop.get_moves(game_board)
        self.assertEqual(moves["moves"], ["E7", "D6", "C5", "B4", "A3"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_bC1(self): 
        game_board = GameBoard(mvmt_board_2)
        bishop = game_board.get_piece_at_position("C1")
        moves = bishop.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B2", "A3", "D2", "E3", "F4", "G5", "H6"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_bF1(self): 
        game_board = GameBoard(mvmt_board_2)
        bishop = game_board.get_piece_at_position("F1")
        moves = bishop.get_moves(game_board)
        self.assertEqual(moves["moves"], ["E2", "G2"])
        self.assertEqual(moves["captures"], ["H3"])

    def test_moves_mb3_bC8(self): 
        game_board = GameBoard(mvmt_board_3)
        bishop = game_board.get_piece_at_position("C8")
        moves = bishop.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B7", "A6", "D7", "E6"])
        self.assertEqual(moves["captures"], ["F5"])

    def test_moves_mb3_bG6(self): 
        game_board = GameBoard(mvmt_board_3)
        bishop = game_board.get_piece_at_position("G6")
        moves = bishop.get_moves(game_board)
        self.assertEqual(moves["moves"], ["F7"])
        self.assertEqual(moves["captures"], ["H7", "F5"])

    def test_moves_mb3_bC1(self): 
        game_board = GameBoard(mvmt_board_3)
        bishop = game_board.get_piece_at_position("C1")
        moves = bishop.get_moves(game_board)
        self.assertEqual(moves["moves"], ["D2", "E3", "F4", "G5", "H6"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb3_bF1(self): 
        game_board = GameBoard(mvmt_board_3)
        bishop = game_board.get_piece_at_position("F1")
        moves = bishop.get_moves(game_board)
        self.assertEqual(moves["moves"], ["G2", "H3"])
        self.assertEqual(moves["captures"], ["E2"])

    def test_moves_mb4_bB5(self): 
        game_board = GameBoard(mvmt_board_4)
        bishop = game_board.get_piece_at_position("B5")
        moves = bishop.get_moves(game_board)
        self.assertEqual(moves["moves"], ["C6", "D7", "E8", "A4", "C4"])
        self.assertEqual(moves["captures"], ["D3"])

    def test_moves_mb4_bD4(self): 
        game_board = GameBoard(mvmt_board_4)
        bishop = game_board.get_piece_at_position("D4")
        moves = bishop.get_moves(game_board)
        self.assertEqual(moves["moves"], ["C5", "B6", "A7", "E5", "F6", "C3"])
        self.assertEqual(moves["captures"], ["G7", "B2", "E3"])
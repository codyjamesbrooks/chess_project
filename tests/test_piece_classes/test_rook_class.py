import unittest
# Boards imports
from chess.gameboard.game_board import GameBoard
# Piece imports
from chess.pieces.rook import Rook
from tests.test_resources.test_boards import test_boards
inital_setup = test_boards[0]
mvmt_board_1 = test_boards[1]
mvmt_board_2 = test_boards[2]
mvmt_board_3 = test_boards[3]
mvmt_board_4 = test_boards[4]

class TestRookClass(unittest.TestCase):
    def test_init_red_rook(self): 
        test_rook = Rook("red", "A8")
        self.assertEqual(test_rook.name, "Rook")
        self.assertEqual(test_rook.alias, "R")
        self.assertEqual(test_rook.color, "red")
        self.assertEqual(test_rook.position, "A8")
        self.assertEqual(test_rook.current_col, "A")
        self.assertEqual(test_rook.current_row, "8")

    def test_get_moves_on_inital_setup(self): 
        # Every Rook in the inital setup should have no possible moves
        # and 0 possible captures. 
        game_board = GameBoard(inital_setup)
        positions = ["A8", "H8", "A1", "H1"]
        for position in positions: 
            rook = game_board.get_piece_at_position(position)
            moves = rook.get_moves(game_board)
            self.assertEqual(moves["moves"], [])
            self.assertEqual(moves["captures"], [])

    def test_moves_mb1_rA8(self): 
        game_board = GameBoard(mvmt_board_1)
        rook = game_board.get_piece_at_position("A8")
        moves = rook.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B8", "C8"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb1_rG8(self): 
        game_board = GameBoard(mvmt_board_1)
        rook = game_board.get_piece_at_position("G8")
        moves = rook.get_moves(game_board)
        self.assertEqual(moves["moves"], ["F8", "G7"])
        self.assertEqual(moves["captures"], [])       

    def test_moves_mb1_rB4(self): 
        game_board = GameBoard(mvmt_board_1)
        rook = game_board.get_piece_at_position("B4")
        moves = rook.get_moves(game_board)
        self.assertEqual(moves["moves"], ["A4", "B3", "B5", "B6"])
        self.assertEqual(moves["captures"], ["B7"])
          
    def test_moves_mb1_rF3(self): 
        game_board = GameBoard(mvmt_board_1)
        rook = game_board.get_piece_at_position("F3")
        moves = rook.get_moves(game_board)
        self.assertEqual(moves["moves"], ["E3", "D3", "G3", "H3", "F2", "F1", "F4", "F5"])
        self.assertEqual(moves["captures"], []) 

    # Only tested the rook in pos H8 on mb2, the other rooks are in inital pos
    def test_moves_mb2_rH8(self): 
        game_board = GameBoard(mvmt_board_2)
        rook = game_board.get_piece_at_position("H8")
        moves = rook.get_moves(game_board)
        self.assertEqual(moves["moves"], ["H7", "H6", "H5", "H4"])
        self.assertEqual(moves["captures"], []) 

    def test_moves_mb3_rH5(self): 
        game_board = GameBoard(mvmt_board_3)
        rook = game_board.get_piece_at_position("H5")
        moves = rook.get_moves(game_board)
        self.assertEqual(moves["moves"], ["G5", "H4", "H3", "H2", "H6"])
        self.assertEqual(moves["captures"], ["F5", "H1", "H7"]) 

    def test_moves_mb3_rH1(self): 
        game_board = GameBoard(mvmt_board_3)
        rook = game_board.get_piece_at_position("H1")
        moves = rook.get_moves(game_board)
        self.assertEqual(moves["moves"], ["G1", "H2", "H3", "H4"])
        self.assertEqual(moves["captures"], ["H5"]) 
    
    def test_moves_mb3_rA8(self): 
        game_board = GameBoard(mvmt_board_3)
        rook = game_board.get_piece_at_position("A8")
        moves = rook.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B8"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb3_rA1(self): 
        game_board = GameBoard(mvmt_board_3)
        rook = game_board.get_piece_at_position("A1")
        moves = rook.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], ["A2"])

    def test_moves_mb4_rC8(self): 
        game_board = GameBoard(mvmt_board_4)
        rook = game_board.get_piece_at_position("C8")
        moves = rook.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B8", "A8", "C7", "C6", "C5", "C4", "C3"])
        self.assertEqual(moves["captures"], ["C2"])

    def test_moves_mb4_rD8(self): 
        game_board = GameBoard(mvmt_board_4)
        rook = game_board.get_piece_at_position("D8")
        moves = rook.get_moves(game_board)
        self.assertEqual(moves["moves"], ["E8", "F8", "D7", "D6", "D5"])
        self.assertEqual(moves["captures"], ["D4"])

    def test_moves_mb4_rA1(self): 
        game_board = GameBoard(mvmt_board_4)
        rook = game_board.get_piece_at_position("A1")
        moves = rook.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B1", "C1", "A2"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb4_rD1(self): 
        game_board = GameBoard(mvmt_board_4)
        rook = game_board.get_piece_at_position("D1")
        moves = rook.get_moves(game_board)
        self.assertEqual(moves["moves"], ["C1", "B1", "E1", "F1", "D2"])
        self.assertEqual(moves["captures"], [])

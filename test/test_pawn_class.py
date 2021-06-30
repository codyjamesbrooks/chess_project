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
inital_setup = test_boards[0]
mvmt_board_1 = test_boards[1]
mvmt_board_2 = test_boards[2]
mvmt_board_3 = test_boards[3]

class TestPawnClass(unittest.TestCase):
    def test_init_red_pawn(self): 
        test_pawn = Pawn("red", "A8")
        self.assertEqual(test_pawn.name, "Pawn")
        self.assertEqual(test_pawn.alias, "P")
        self.assertEqual(test_pawn.color, "red")
        self.assertEqual(test_pawn.position, "A8")
        self.assertEqual(test_pawn.current_col, "A")
        self.assertEqual(test_pawn.current_row, "8")

    def test_get_moves_method_on_pawns_inital_setup(self): 
        # Every Pawn in the inital setup should have two possible moves
        # and 0 possible captures. 
        game_board = GameBoard(inital_setup)
        for row in game_board.pieces: 
            for piece in row: 
                if piece.name == "Pawn": 
                    moves = piece.get_moves(game_board)
                    self.assertEqual(len(moves["moves"]), 2)
                    self.assertEqual(len(moves["captures"]), 0)

    # Test the get_moves result for every pawn in mvmt_board_1
    def test_moves_mb1_pA7(self): 
        game_board = GameBoard(mvmt_board_1)
        pawn = game_board.get_piece_at_position("A7")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["A6"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb1_pB7(self): 
        game_board = GameBoard(mvmt_board_1)
        pawn = game_board.get_piece_at_position("B7")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B6", "B5"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb1_pF7(self): 
        game_board = GameBoard(mvmt_board_1)
        pawn = game_board.get_piece_at_position("F7")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb1_pH7(self): 
        game_board = GameBoard(mvmt_board_1)
        pawn = game_board.get_piece_at_position("H7")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["H6", "H5"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb1_pE6(self): 
        game_board = GameBoard(mvmt_board_1)
        pawn = game_board.get_piece_at_position("E6")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb1_pF6(self): 
        game_board = GameBoard(mvmt_board_1)
        pawn = game_board.get_piece_at_position("F6")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb1_pG6(self): 
        game_board = GameBoard(mvmt_board_1)
        pawn = game_board.get_piece_at_position("G6")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["G5"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb1_pE4(self): 
        game_board = GameBoard(mvmt_board_1)
        pawn = game_board.get_piece_at_position("E4")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb1_pC3(self): 
        game_board = GameBoard(mvmt_board_1)
        pawn = game_board.get_piece_at_position("C3")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb1_pB2(self): 
        game_board = GameBoard(mvmt_board_1)
        pawn = game_board.get_piece_at_position("B2")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B3"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb1_pG2(self): 
        game_board = GameBoard(mvmt_board_1)
        pawn = game_board.get_piece_at_position("G2")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["G3", "G4"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb1_pH2(self): 
        game_board = GameBoard(mvmt_board_1)
        pawn = game_board.get_piece_at_position("H2")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["H3"])
        self.assertEqual(moves["captures"], [])

    # Test the get_moves result for every pawn in mvmt_board_2
    def test_moves_mb2_pA7(self): 
        game_board = GameBoard(mvmt_board_2)
        pawn = game_board.get_piece_at_position("A7")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["A6", "A5"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_pB5(self): 
        game_board = GameBoard(mvmt_board_2)
        pawn = game_board.get_piece_at_position("B5")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B4"])
        self.assertEqual(moves["captures"], ["C4"])

    def test_moves_mb2_pC6(self): 
        game_board = GameBoard(mvmt_board_2)
        pawn = game_board.get_piece_at_position("C6")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["C5"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_pD7(self): 
        game_board = GameBoard(mvmt_board_2)
        pawn = game_board.get_piece_at_position("D7")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["D6", "D5"])
        self.assertEqual(moves["captures"], [])   

    def test_moves_mb2_pE5(self): 
        game_board = GameBoard(mvmt_board_2)
        pawn = game_board.get_piece_at_position("E5")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], [])    

    def test_moves_mb2_pF5(self): 
        game_board = GameBoard(mvmt_board_2)
        pawn = game_board.get_piece_at_position("F5")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["F4"])
        self.assertEqual(moves["captures"], ["E4"])

    def test_moves_mb2_pG7(self): 
        game_board = GameBoard(mvmt_board_2)
        pawn = game_board.get_piece_at_position("G7")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["G6", "G5"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_pH3(self): 
        game_board = GameBoard(mvmt_board_2)
        pawn = game_board.get_piece_at_position("H3")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_pA2(self): 
        game_board = GameBoard(mvmt_board_2)
        pawn = game_board.get_piece_at_position("A2")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["A3", "A4"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_pB3(self): 
        game_board = GameBoard(mvmt_board_2)
        pawn = game_board.get_piece_at_position("B3")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B4"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_pC4(self): 
        game_board = GameBoard(mvmt_board_2)
        pawn = game_board.get_piece_at_position("C4")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["C5"])
        self.assertEqual(moves["captures"], ["B5"])

    def test_moves_mb2_pD3(self): 
        game_board = GameBoard(mvmt_board_2)
        pawn = game_board.get_piece_at_position("D3")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["D4"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_pE4(self): 
        game_board = GameBoard(mvmt_board_2)
        pawn = game_board.get_piece_at_position("E4")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], ["F5"])

    def test_moves_mb2_pF3(self): 
        game_board = GameBoard(mvmt_board_2)
        pawn = game_board.get_piece_at_position("F3")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["F4"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_pG3(self): 
        game_board = GameBoard(mvmt_board_2)
        pawn = game_board.get_piece_at_position("G3")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["G4"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb2_pH2(self): 
        game_board = GameBoard(mvmt_board_2)
        pawn = game_board.get_piece_at_position("H2")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], [])

    # Test the get_moves result for every pawn in mvmt_board_3
    def test_moves_mb3_pA3(self):
        game_board = GameBoard(mvmt_board_3)
        pawn = game_board.get_piece_at_position("A3")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], ["B2"])

    def test_moves_mb3_pA2(self):
        game_board = GameBoard(mvmt_board_3)
        pawn = game_board.get_piece_at_position("A2")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], ["B1"])

    def test_moves_mb3_pB6(self):
        game_board = GameBoard(mvmt_board_3)
        pawn = game_board.get_piece_at_position("B6")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["B7"])
        self.assertEqual(moves["captures"], ["A7", "C7"])

    def test_moves_mb3_pB4(self):
        game_board = GameBoard(mvmt_board_3)
        pawn = game_board.get_piece_at_position("B4")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb3_pB3(self):
        game_board = GameBoard(mvmt_board_3)
        pawn = game_board.get_piece_at_position("B3")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb3_mb3(self):
        game_board = GameBoard(mvmt_board_3)
        pawn = game_board.get_piece_at_position("B2")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], ["A3"])

    def test_moves_mb3_pC7(self):
        game_board = GameBoard(mvmt_board_3)
        pawn = game_board.get_piece_at_position("C7")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], ["B6", "D6"])

    def test_moves_mb3_pC6(self):
        game_board = GameBoard(mvmt_board_3)
        pawn = game_board.get_piece_at_position("C6")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["C5"])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb3_pC2(self):
        game_board = GameBoard(mvmt_board_3)
        pawn = game_board.get_piece_at_position("C2")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], ["B1", "D1"])

    def test_moves_mb3_pD6(self):
        game_board = GameBoard(mvmt_board_3)
        pawn = game_board.get_piece_at_position("D6")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["D7"])
        self.assertEqual(moves["captures"], ["C7"])

    def test_moves_mb3_pE7(self):
        game_board = GameBoard(mvmt_board_3)
        pawn = game_board.get_piece_at_position("E7")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb3_pE4(self):
        game_board = GameBoard(mvmt_board_3)
        pawn = game_board.get_piece_at_position("E4")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb3_pE2(self):
        game_board = GameBoard(mvmt_board_3)
        pawn = game_board.get_piece_at_position("E2")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], ["D1", "F1"])

    def test_moves_mb3_pF5(self):
        game_board = GameBoard(mvmt_board_3)
        pawn = game_board.get_piece_at_position("F5")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], ["G6"])

    def test_moves_mb3_pG7(self):
        game_board = GameBoard(mvmt_board_3)
        pawn = game_board.get_piece_at_position("G7")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], [])
        self.assertEqual(moves["captures"], [])

    def test_moves_mb3_pH7(self):
        game_board = GameBoard(mvmt_board_3)
        pawn = game_board.get_piece_at_position("H7")
        moves = pawn.get_moves(game_board)
        self.assertEqual(moves["moves"], ["H8"])
        self.assertEqual(moves["captures"], [])

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
import unittest
from chess.gameboard.game_board import GameBoard
from chess.gameboard.analyze_board import AnalyzeBoard

# piece imports
from chess.pieces.king import King

from test.test_boards.test_boards import test_boards
inital_setup = test_boards[0]
mvmt_board_1 = test_boards[1]
mvmt_board_2 = test_boards[2]
mvmt_board_3 = test_boards[3]
mvmt_board_4 = test_boards[4]

class TestAnalyzeBoardClass(unittest.TestCase): 
    def setUp(self): 
        self.analyze = AnalyzeBoard()

    def test_locate_colors_king_method_inital_setup(self): 
        game_board = GameBoard(inital_setup)
        red_king = self.analyze.locate_colors_king("red", game_board)
        blue_king = self.analyze.locate_colors_king("blue", game_board)

        self.assertEqual(red_king, King("red", "E1"))
        self.assertEqual(blue_king, King("blue", "E8"))

    def test_locate_colors_king_mb1(self): 
        game_board = GameBoard(mvmt_board_1)
        red_king = self.analyze.locate_colors_king("red", game_board)
        blue_king = self.analyze.locate_colors_king("blue", game_board)

        self.assertEqual(red_king, King("red", "H1"))
        self.assertEqual(blue_king, King("blue", "H8"))


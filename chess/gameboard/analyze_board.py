# Board import 
from chess.gameboard.game_board import GameBoard
from chess.gameboard.empty_space import Empty_Space

# Piece imports
from chess.pieces.bishop import Bishop
from chess.pieces.king import King
from chess.pieces.knight import Knight 
from chess.pieces.pawn import Pawn 
from chess.pieces.queen import Queen
from chess.pieces.rook import Rook 

class AnalyzeBoard:
    def is_color_king_check(self, color, game_board): 
        opponents_pieces = [piece for row in game_board for piece in row if 
                            piece.color != color and piece != Empty_Space()]

        king_position = self.locate_colors_king(color, game_board).position
        
        for piece in opponents_pieces: 
            piece_moves = piece.get_moves(game_board)
            if king_position in piece_moves["captures"]: 
                return True
        return False

    def locate_colors_king(self, color, game_board): 
        # given a piece color, and a game_board. return the king piece 
        for row in game_board.pieces: 
            for piece in row: 
                if piece.name == "King" and piece.color == color: 
                    king = piece
        return king


    





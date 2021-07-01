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
    def is_color_in_check(self, color, game_board): 
        opponents_pieces = [piece for row in game_board.pieces for piece in row if 
                            piece.color != color and piece != Empty_Space()]

        king_position = self.locate_colors_king(color, game_board).position
        
        # king is in check when there exist any opponent piece that could 
        # move to the kings current position. i.e. capture the king.  
        for piece in opponents_pieces: 
            piece_moves = piece.get_moves(game_board)
            if king_position in piece_moves["captures"]: 
                return True
        return False

    def is_color_in_checkmate(self, color, game_board): 
        opponents_pieces = [piece for row in game_board.pieces for pieces in row if
                            piece.color != color and piece != Empty_Space()]

        king = self.locate_colors_king(color, game_board)
        king_moves = king.get_moves(game_board)

        # king is in checkmate when there exists no squares in which the king could 
        # travel to that is not being targeted by an opponent. 
        target_squares = []
        for piece in oppenents_pieces:
            piece_moves = piece.get_moves(game_board)
            target_squares += pieces_moves["moves"]

        # This method still needs work!
        # I need to handle modifying the game_board.pieces array in order to chase down all the potential
        # captures the king could make. 
        return False

    def locate_colors_king(self, color, game_board): 
        # given a piece color, and a game_board. return the king piece 
        for row in game_board.pieces: 
            for piece in row: 
                if piece.name == "King" and piece.color == color: 
                    king = piece
        return king

    def is_player_move_valid(self, color, check_status, player_move):
        move_validity = { "valid": False, "invalid_msg": "" }
        # Validating a player move is a 3 step process. 
        # 1. Find the piece that the player would like to move 

        return move_validity

        
        
# is_player_move_valid(color, player_move)


    





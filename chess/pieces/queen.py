from chess.pieces.piece import Piece
from chess.pieces.rook import Rook
from chess.pieces.bishop import Bishop

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.name = "Queen"
        self.alias = "Q"

    def get_moves(self, game_board):
        # Queens move like Rooks, and Bishops combined. 
        # So we can instinate a rook, and bishop with the same color/pos as the queen 
        # then combine their moves dicts to form the queens moves dict 
        temp_rook = Rook(self.color, self.position)
        rook_like_moves = temp_rook.get_moves(game_board)

        temp_bishop = Bishop(self.color, self.position)
        bishop_like_moves = temp_bishop.get_moves(game_board)

        move_directions = [rook_like_moves, bishop_like_moves]
        moves = { "moves": [], "captures": [] }
        for key in moves.keys():
            for direction in move_directions: 
                moves[key] += direction[key]

        return moves
 
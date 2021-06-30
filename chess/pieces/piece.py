from chess.gameboard.empty_space import Empty_Space

class Piece:
    def __init__(self, color, position):
        self.name = None
        self.color = color
        self.position = position
        self.columns = "ABCDEFGH"  # Used for indexing and finding potential moves

        self.current_col = position[0] 
        self.current_row = position[1]

    def __repr__(self):
        return f"{self.color.title()} {self.name}"

    def __eq__(self, other): 
        return ( self.name == other.name and
                 self.color == other.color and
                 self.position == self.position )

    def update_moves_based_on_encountered_piece(self, moves, board_piece, position):
        # Use an array with two indexs. One is a Bool that will comunicate if continued mvmt is possible
        # The second index will be a copy of the provided moves dict. 
        updated_moves = [False, { "moves": moves["moves"], "captures": moves["captures"] }]
        
        if board_piece == Empty_Space():
            updated_moves[0]  =  True # continued mvmt is possible
            updated_moves[1]["moves"].append(position)
        elif board_piece.color != self.color: 
            updated_moves[1]["captures"].append(position)

        return updated_moves


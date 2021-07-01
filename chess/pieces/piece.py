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

    def set_position(self, new_position):
        # Used to update a pieces position
        self.position = new_position
        self.current_col = new_position[0]
        self.current_row = new_position[1]

    def update_moves_based_on_encountered_piece(self, moves, board_piece, position):
        # This method is used when a piece is moving. Each piece has the ability to call it when it is trying to 
        # determine its available moves. It will return to them an updated dict with the position in question 
        # added or not. And a bool indicating if the piece can keep moving (if it can move in that fashion). 
        updated_moves = [False, { "moves": moves["moves"], "captures": moves["captures"] }]

        if board_piece == Empty_Space():
            updated_moves[0]  =  True # continued mvmt is possible
            updated_moves[1]["moves"].append(position)
        elif board_piece.color != self.color: 
            updated_moves[1]["captures"].append(position)

        return updated_moves


from chess.gameboard.empty_space import Empty_Space
from chess.pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.name = "Pawn"
        self.alias = "P"

    def get_moves(self, game_board):
        # given a game board, return the potential moves and captures that a pawn could make
        moves = { "moves": self.get_column_moves(game_board),
                  "captures": self.get_captures(game_board)   }
        return moves

    def get_column_moves(self, game_board): 
        col_index = self.columns.index(self.current_col)
        moves = []

        dir_of_travel = {"blue": -1, "red": 1}[self.color]
        new_row = dir_of_travel + int(self.current_row) 
        
        if game_board.get_piece_at_position(f"{self.current_col}{new_row}") == Empty_Space(): 
            moves.append(f"{self.current_col}{new_row}")

        # conditionally allow for double move if pawn is in start pos
        # and if the space directly in front was unoccupied. 
        start = { "blue": "7", "red": "2" }
        if self.current_row == start[self.color] and len(moves) > 0:
            new_row = 2 * dir_of_travel + int(self.current_row)
            if game_board.get_piece_at_position(f"{self.current_col}{new_row}") == Empty_Space():
                moves.append(f"{self.current_col}{new_row}")
        
        return moves

    def get_captures(self, game_board):
        # Using the pawns current position, determine the potential captures that it could make
        col_index = self.columns.index(self.current_col)
        potential_caps = []

        # Create a string of the with the columns the pawn could capture in
        potential_cols = self.columns[max(col_index - 1, 0) : col_index + 2]
        potential_cols = potential_cols.replace(self.current_col, "")
        
        # Capture_row is the row the pawn should check for captures
        capture_row = int(self.current_row) + {"blue": -1, "red": 1}[self.color]
        
        # List of the squares the pawn could capture an enemy piece in
        capture_squares = [f"{col}{str(capture_row)}" for col in list(potential_cols)]
        for square in capture_squares:
            # Check each capture square to see if an enemy piece is there
            board_piece = game_board.get_piece_at_position(square)
            if board_piece != Empty_Space() and board_piece.color != self.color: 
                potential_caps.append(square)
        
        return potential_caps


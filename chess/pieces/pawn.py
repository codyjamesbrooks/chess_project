from chess.gameboard.empty_space import Empty_Space
from chess.pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        self.name = "Pawn"
        self.alias = "P"
        self.color = color
        self.position = position

    def get_moves(self, game_board):
        # given a game board, return the potential moves and captures that a pawn could make
        moves = { "moves": self.get_column_moves(game_board),
                  "captures": self.get_captures(game_board)   }
        return moves

    def get_column_moves(self, game_board): 
        current_col, current_row = list(self.position)
        col_index = self.columns.index(current_col)
        moves = []

        dir_of_travel = {"blue": -1, "red": 1}[self.color]
        new_row = dir_of_travel + int(current_row) 
        
        if game_board.get_piece_at_position(f"{current_col}{new_row}") == Empty_Space(): 
            moves.append(f"{current_col}{new_row}")

        # conditionally allow for double move if pawn is in start pos
        start = { "blue": 7, "red": 2 }
        if int(current_row) == start[self.color]:
            new_row = 2 * dir_of_travel + int(current_row)
            if game_board.get_piece_at_position(f"{current_col}{new_row}") == Empty_Space():
                moves.append(f"{current_col}{new_row}")
        
        return moves

    def get_captures(self, game_board):
        # Using the pawns current position, determine the potential captures that it could make
        current_col, current_row = list(self.position)
        col_index = self.columns.index(current_col)
        potential_caps = []

        # Create a string of the with the columns the pawn could capture in
        potential_cols = self.columns[max(col_index - 1, 0) : col_index + 2]
        potential_cols = potential_cols.replace(current_col, "")
        
        # Capture_row is the row the pawn should check for captures
        capture_row = int(current_row) + {"blue": -1, "red": 1}[self.color]
        
        # List of the squares the pawn could capture an enemy piece in
        capture_squares = [f"{col}{str(capture_row)}" for col in list(potential_cols)]
        for square in capture_squares:
            # Check each capture square to see if an enemy piece is there
            board_piece = game_board.get_piece_at_position(square)
            if board_piece != Empty_Space() and board_piece.color != self.color: 
                potential_caps.append(square)
        
        return potential_caps


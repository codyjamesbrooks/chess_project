from chess.pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        self.name = "Pawn"
        self.alias = "P"
        self.color = color
        self.position = position

    def get_potential_moves(self, game_board):
        # given a game baord, return the potential moves that can be made by a pawn at self.position
        current_col, current_row = list(self.position)
        col_index = self.columns.index(current_col)

        dir_of_travel = {"blue": -1, "red": 1}[self.color]
        moves = [f"{current_col}{dir_of_travel + int(current_row)}"]

        start = {
            "blue": 7,
            "red": 2,
        }  # Add in optional move if the pawn is in its start pos
        if int(current_row) == start[self.color]:
            moves.append(f"{current_col}{(2 * dir_of_travel) + int(current_row)}")

        return moves

    def get_potential_caputures(self):
        # Using the pawns current position, determine the potential captures that it could make
        current_col, current_row = list(self.position)
        col_index = self.columns.index(current_col)

        potential_cols = self.columns[max(col_index - 1, 0) : col_index + 2]
        allowed_row = int(current_row) + {"blue": -1, "red": 1}[self.color]

        potential_moves = [col + str(allowed_row) for col in list(potential_cols)]
        return potential_moves

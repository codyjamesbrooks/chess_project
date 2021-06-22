from chess.pieces.piece import Piece


class King(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        self.name = "King"
        self.alias = "K"

    def get_potential_moves(self):
        current_col, current_row = list(self.position)
        col_index = self.columns.index(current_col)
        current_row = int(current_row)

        potential_cols = self.columns[max(col_index - 1, 0) : col_index + 2]
        potential_rows = list(range(max(current_row - 1, 1), min(current_row + 2, 9)))
        potential_moves = [
            f"{col}{row}"
            for row in potential_rows
            for col in potential_cols
            if f"{col}{row}" != self.position
        ]
        return potential_moves

from chess.pieces.piece import Piece


class Rook(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        self.name = "Rook"
        self.alias = "R"

    def get_potential_moves(self):
        current_col, current_row = list(self.position)
        col_index = self.columns.index(current_col)

        # Create array of moves for each direction of travel. Order of elements is expands
        # from the Rooks current position
        col_moves_left = [
            f"{col}{current_row}" for col in self.columns[col_index - 1 :: -1]
        ]
        col_moves_right = [
            f"{col}{current_row}" for col in self.columns[col_index + 1 :]
        ]
        row_moves_up = [f"{current_col}{row}" for row in range(int(current_row) + 1, 9)]
        row_moves_down = [
            f"{current_col}{row}" for row in range(int(current_row) - 1, 0, -1)
        ]

        potential_moves = [
            col_moves_left,
            col_moves_right,
            row_moves_up,
            row_moves_down,
        ]
        return [moves for moves in potential_moves if len(moves) > 0]

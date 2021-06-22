from chess.pieces.piece import Piece


class Queen(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        self.name = "Queen"
        self.alias = "Q"

    def get_potential_moves(self):
        # Returns arrays of squares expanding from the current position of the queens position.
        current_col, current_row = list(self.position)
        col_index = self.columns.index(current_col)
        row_num = int(current_row)

        # Moves along same row/column - same method as used in Rook class
        col_moves_left = [
            f"{col}{current_row}" for col in self.columns[col_index - 1 :: -1]
        ]
        col_moves_right = [
            f"{col}{current_row}" for col in self.columns[col_index + 1 :]
        ]
        row_moves_up = [f"{current_col}{row}" for row in range(row_num + 1, 9)]
        row_moves_down = [f"{current_col}{row}" for row in range(row_num - 1, 0, -1)]

        # Moves along Diagionals - same method as used in Bishop class
        diag_1 = []  # Moving towards A8
        for i, row in enumerate(range(row_num + 1, 9)):
            if col_index - i - 1 < 0:
                break
            diag_1.append(f"{self.columns[col_index - i - 1]}{row}")

        diag_2 = []  # Moving towards H8
        for i, row in enumerate(range(row_num + 1, 9)):
            if col_index + i + 1 > 7:
                break
            diag_2.append(f"{self.columns[col_index + i + 1]}{row}")

        diag_3 = []  # Moving towards H1
        for i, row in enumerate(range(row_num - 1, 0, -1)):
            if col_index + i + 1 > 7:
                break
            diag_3.append(f"{self.columns[col_index + i + 1]}{row}")

        diag_4 = []  # Moving towards A1
        for i, row in enumerate(range(row_num - 1, 0, -1)):
            if col_index - i - 1 < 0:
                break
            diag_4.append(f"{self.columns[col_index - i - 1]}{row}")

        potential_moves = [
            col_moves_left,
            col_moves_right,
            row_moves_up,
            row_moves_down,
            diag_1,
            diag_2,
            diag_3,
            diag_4,
        ]

        return [moves for moves in potential_moves if len(moves) > 0]

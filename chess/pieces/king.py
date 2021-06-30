from chess.pieces.piece import Piece


class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.name = "King"
        self.alias = "K"

    def get_moves(self, game_board):
        col_index = self.columns.index(self.current_col)
        row_num = int(self.current_row)

        potential_cols = self.columns[max(col_index - 1, 0) : col_index + 2]
        potential_rows = list(range(max(row_num - 1, 1), min(row_num + 2, 9)))
        moves = { "moves": [], "captures": [] }
 
        for col in potential_cols:
            for row in potential_rows:
                pos_to_check = f"{col}{row}" 
                if pos_to_check != self.position:
                    board_piece = game_board.get_piece_at_position(pos_to_check)
                    _, moves = self.update_moves_based_on_encountered_piece(moves, board_piece, pos_to_check)

        return moves


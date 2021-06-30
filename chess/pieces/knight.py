from chess.pieces.piece import Piece
from chess.gameboard.empty_space import Empty_Space

class Knight(Piece): 
    def __init__(self, color, position=None): 
        super().__init__(color, position)
        self.name = "Knight"
        self.alias = "N"
        
    def get_moves(self, game_board): 
        # given game_board, return moves/captures dict for a Knight at any poistion on the board. 
        col_index = self.columns.index(self.current_col)
        row_num = int(self.current_row)
        moves = { "moves": [], "captures": [] }

        col_row_changes = [(-2, 1), (-1, 2), (1, 2), (2, 1),
                           (2, -1), (1, -2), (-1, -2), (-2, -1)]

        for col, row in col_row_changes:
            new_col = col_index + col
            new_row = row_num + row
            if ( 0 <= new_col <= 7 and
                 1 <= new_row <= 8  ):
                pos_to_check = f"{self.columns[new_col]}{new_row}"
                board_piece = game_board.get_piece_at_position(pos_to_check)

                # we can still use the update_moves_based_on_encountered_piece_method
                # But we can discard the keep moving bool, as the knight doesn't move linearly
                _ , moves = self.update_moves_based_on_encountered_piece(moves, board_piece, pos_to_check) 
        return moves








    def get_potential_moves(self):
        current_col, current_row = list(self.position)
        col_index = self.columns.index(current_col)
        row_index = int(current_row)
        
        potential_moves = []
        col_row_changes = [(-2, 1), (-1, 2), (1, 2), (2, 1),
                           (2, -1), (1, -2), (-1, -2), (-2, -1)]
        
        
        for col_change, row_change in col_row_changes:
            new_col = col_index + col_change
            new_row = row_index + row_change
            if  (0 <= new_col <= 7 and
                 1 <= new_row <= 8): 
                potential_moves.append(f"{self.columns[new_col]}{new_row}")
        return potential_moves
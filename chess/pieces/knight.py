from chess.pieces.piece import Piece

class Knight(Piece): 
    def __init__(self, color, position=None): 
        super().__init__(color, position)
        self.name = "Knight"
        self.alias = "N"
        
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
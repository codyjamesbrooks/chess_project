from chess.pieces.piece import Piece
from chess.gameboard.empty_space import Empty_Space

class Bishop(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        self.name = "Bishop"
        self.alias = "B"

    def get_moves(self, game_board): 
        neg_cols_pos_rows = self.get_neg_cols_pos_rows_moves(game_board)
        pos_cols_pos_rows = self.get_pos_cols_pos_rows_moves(game_board)
        neg_cols_neg_rows = self.get_neg_cols_neg_rows_moves(game_board)
        pos_cols_neg_rows = self.get_pos_cols_neg_rows_moves(game_board)

        move_directions = [neg_cols_pos_rows, pos_cols_pos_rows, neg_cols_neg_rows, pos_cols_neg_rows]
        moves = { "moves": [], "captures": [] }
        for key in moves.keys(): 
            for direction in move_directions: 
                moves[key] += direction[key]
        return moves

    def get_neg_cols_pos_rows_moves(self, game_board):
        moves = { "moves": [], "captures": [] }
        row_num = int(self.current_row)
        col_index = self.columns.index(self.current_col)
        for i, row in enumerate(range(row_num + 1, 9)):
            if col_index - i - 1 < 0:
                break

            pos_to_check = f"{self.columns[col_index - i - 1]}{row}"
            board_piece = game_board.get_piece_at_position(pos_to_check)
            keep_moving, moves = self.update_moves_based_on_encountered_piece(moves, board_piece, pos_to_check)
            if keep_moving == False: 
                break
        return moves

    def get_pos_cols_pos_rows_moves(self, game_board):
        moves = { "moves": [], "captures": [] }
        row_num = int(self.current_row)
        col_index = self.columns.index(self.current_col)
        for i, row in enumerate(range(row_num + 1, 9)): 
            if col_index + i + 1 > 7: 
                break

            pos_to_check = f"{self.columns[col_index + i + 1]}{row}"
            board_piece = game_board.get_piece_at_position(pos_to_check)
            keep_moving, moves = self.update_moves_based_on_encountered_piece(moves, board_piece, pos_to_check)
            
            if keep_moving == False: 
                break
        return moves

    def get_neg_cols_neg_rows_moves(self, game_board):
        moves = { "moves": [], "captures": [] }
        row_num = int(self.current_row)
        col_index = self.columns.index(self.current_col)
        for i, row in enumerate(range(row_num - 1, 0, -1)): 
            if col_index - i - 1 < 0: 
                break

            pos_to_check = f"{self.columns[col_index - i - 1]}{row}"
            board_piece = game_board.get_piece_at_position(pos_to_check)
            keep_moving, moves = self.update_moves_based_on_encountered_piece(moves, board_piece, pos_to_check)
            
            if keep_moving == False: 
                break
        return moves

    def get_pos_cols_neg_rows_moves(self, game_board):
        moves = { "moves": [], "captures": [] }
        row_num = int(self.current_row)
        col_index = self.columns.index(self.current_col)
        for i, row in enumerate(range(row_num - 1, 0, -1)): 
            if col_index + i + 1 > 7: 
                break

            pos_to_check = f"{self.columns[col_index + i + 1]}{row}"
            board_piece = game_board.get_piece_at_position(pos_to_check)
            keep_moving, moves = self.update_moves_based_on_encountered_piece(moves, board_piece, pos_to_check)
            
            if keep_moving == False: 
                break
        return moves


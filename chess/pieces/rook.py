from chess.pieces.piece import Piece
from chess.gameboard.empty_space import Empty_Space

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.name = "Rook"
        self.alias = "R"

    def get_moves(self, game_board):
        # given a game board, return the potential moves and captures that a rook could make
        # create moves dict for the row and col movement. 
        row_moves = self.get_row_moves(game_board)
        col_moves = self.get_col_moves(game_board)

        # combine the two dicts
        move_directions = [row_moves, col_moves]
        moves = { "moves": [], "captures": [] }
        for key in moves.keys(): 
            for direction in move_directions: 
                moves[key] += direction[key]
        return moves

    def get_row_moves(self, game_board):
        # Used game_board get_pieces_in_row then iterate over it in both directions. 
        game_board_row = game_board.get_pieces_in_row_list(self.current_row)
        col_index = self.columns.index(self.current_col)
        moves = { "moves": [], "captures": [] }

        for col in range(col_index - 1, -1, -1): # traverse cols neg dir
            board_piece = game_board_row[col]
            pos_to_check = f"{self.columns[col]}{self.current_row}"            
            keep_moving, moves = self.update_moves_based_on_encountered_piece(moves, board_piece, pos_to_check)
            if keep_moving == False: 
                break
        
        for col in range(col_index + 1, 8):  # traverse cols pos dir
            board_piece = game_board_row[col]
            pos_to_check = f"{self.columns[col]}{self.current_row}"
            keep_moving, moves = self.update_moves_based_on_encountered_piece(moves, board_piece, pos_to_check)
            if keep_moving == False: 
                break

        return moves

    def get_col_moves(self, game_board):
        # simillar to get_row_moves
        game_board_col = game_board.get_pieces_in_col_list(self.current_col)
        row_index = 8 - int(self.current_row)
        moves = { "moves": [], "captures": [] }

        for row in range(row_index + 1, 8):
            board_piece = game_board_col[row]
            pos_to_check = f"{self.current_col}{8 - row}"
            keep_moving, moves = self.update_moves_based_on_encountered_piece(moves, board_piece, pos_to_check)
            if keep_moving == False: 
                break

        for row in range(row_index - 1, -1, -1): 
            board_piece = game_board_col[row]
            pos_to_check = f"{self.current_col}{8 - row}"
            keep_moving, moves = self.update_moves_based_on_encountered_piece(moves, board_piece, pos_to_check)
            if keep_moving == False: 
                break
        
        return moves


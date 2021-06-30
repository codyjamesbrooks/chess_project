from chess.pieces.piece import Piece
from chess.gameboard.empty_space import Empty_Space

class Rook(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        self.name = "Rook"
        self.alias = "R"

    def get_moves(self, game_board):
        # given a game board, return the potential moves and captures that a rook could make
        neg_col_moves = self.get_neg_col_moves(game_board)
        pos_col_moves = self.get_pos_col_moves(game_board)
        neg_row_moves = self.get_neg_row_moves(game_board)
        pos_row_moves = self.get_pos_row_moves(game_board)

        move_directions = [neg_col_moves, pos_col_moves, neg_row_moves, pos_row_moves]
        moves = { "moves": [], "captures": [] }
        for key in moves.keys(): 
            for direction in move_directions: 
                moves[key] += direction[key]
        return moves


        # Create array of moves for each direction of travel stopping when a occupied square is encountered
    def get_neg_col_moves(self, game_board): 
        col_index = self.columns.index(self.current_col)
        moves = { "moves": [], "captures": [] }
        for col in self.columns[col_index - 1 : : -1]:
            pos_to_check = f"{col}{self.current_row}"
            board_piece = game_board.get_piece_at_position(pos_to_check) 

            if board_piece == Empty_Space(): 
                moves["moves"].append(pos_to_check)
            elif board_piece.color != self.color: 
                moves["captures"].append(pos_to_check)
                break
            else: # Encounterd same colored piece
                break
        return moves

    def get_pos_col_moves(self, game_board): 
        col_index = self.columns.index(self.current_col)
        moves = { "moves": [], "captures": [] }
        for col in self.columns[col_index + 1:]:
            pos_to_check = f"{col}{self.current_row}"
            board_piece = game_board.get_piece_at_position(pos_to_check) 

            if board_piece == Empty_Space(): 
                moves["moves"].append(pos_to_check)
            elif board_piece.color != self.color: 
                moves["captures"].append(pos_to_check)
                break
            else: # Encounterd same colored piece
                break
        return moves

    def get_neg_row_moves(self, game_board): 
        moves = { "moves": [], "captures": [] }
        for row in range(int(self.current_row) - 1, 0, -1):
            pos_to_check = f"{self.current_col}{row}"
            board_piece = game_board.get_piece_at_position(pos_to_check) 

            if board_piece == Empty_Space(): 
                moves["moves"].append(pos_to_check)
            elif board_piece.color != self.color: 
                moves["captures"].append(pos_to_check)
                break
            else: # Encounterd same colored piece
                break
        return moves

    def get_pos_row_moves(self, game_board): 
        moves = { "moves": [], "captures": [] }
        for row in range(int(self.current_row) + 1, 9):
            pos_to_check = f"{self.current_col}{row}"
            board_piece = game_board.get_piece_at_position(pos_to_check) 

            if board_piece == Empty_Space(): 
                moves["moves"].append(pos_to_check)
            elif board_piece.color != self.color: 
                moves["captures"].append(pos_to_check)
                break
            else: # Encounterd same colored piece
                break
        return moves

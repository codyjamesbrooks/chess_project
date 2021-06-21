from chess.square import Square
from chess.empty_space import Empty_Space


class GameBoard:
    def __init__(self, pieces=[[Empty_Space() for _ in range(8)] for _ in range(8)]):
        # initilize a Game Board using a provided pieces array.
        # pieces defaults to an array of empty squares if no pieces are supplied
        square_colors = {
            0: "white",
            1: "black",
            2: "white",
        }  # Dict used to apply color to square backgrounds
        self.cols = "ABCDEFGH"
        self.pieces = pieces
        self.board = []

        # populate self.board with a chess board using the provided pieces array
        for board_row in range(8):
            current_row = []
            for board_column in range(8):
                square_color = square_colors[(board_column % 2) + (board_row % 2)]
                square_label = f"{self.cols[board_column]}{8 - board_row}"
                square_piece = self.pieces[board_row][board_column]
                current_row.append(Square(square_color, square_label, square_piece))
            self.board.append(current_row)

    def __repr__(self):
        display_board = []
        rules = self.rules_sidebar()
        row_counter = 0

        # Assemble the row of squares.
        for row in self.board:
            temp_row = ["", "", ""]
            for square in row:
                temp_row = [x + y for x, y in zip(temp_row, square.assemble_square())]

            # Add in the line of rules
            if row_counter < len(rules):
                temp_row = [
                    x + y
                    for x, y in zip(temp_row, rules[row_counter : row_counter + 3])
                ]
                row_counter += 3
            display_board.append("\n".join(temp_row))

        return "\n".join(display_board) + "\n"

    def rules_sidebar(self):
        side_bar = [
            "A Helpful Guide To Entering Your Moves".center(41),
            "*" * 41,
            "Syntax: From - Piece - To".center(41),
            " Piece Names (Case Insensitive) ".center(40, "*"),
            "King: k".center(20) + "|" + "Queen: q".center(20),
            "Rook: r".center(20) + "|" + "Bishop: b".center(20),
            "Knight: n".center(20) + "|" + "Pawn: p".center(20),
            " Sample Moves ".center(40, "*"),
            "E2-p-E4  =>  ".center(15) + "Pawn at E2 move to E4",
            "F1-n-E3  =>  ".center(15) + "Knight at F1 move to E3",
            "E1-k-D1  =>  ".center(15) + "King at E1 move to D1",
            " Special Moves ".center(41, "*"),
            "- Pawn Promotion:  Indicate returned piece".center(41),
            "B7-p-B8-q  =>  ".center(17) + "Promote pawn to queen",
            "- Castling : Use traditional notation ",
            "O-O  =>  ".center(17) + "Kingside Rook Castle",
            "O-O-O  =>  ".center(17) + "Queenside Rook Castle",
            " Good Luck. Have Fun ".center(41, "*"),
        ]
        return ["\t" + row for row in side_bar]

    def get_piece_at_position(self, position):
        # Given poition in form '(ColumnLetter)(RowNumber)' return the piece at that position
        current_col, current_row = list(position)
        row_index = 8 - int(current_row)
        col_index = self.columns.index(current_col)

        return self.pieces[row_index][col_index]

    def get_pieces_in_col_list(self, column_letter):
        # Given column_letter return a list of pieces in that column.
        col_index = self.columns.index(column_letter)
        pieces_in_col = [self.pieces[row][col_index] for row in range(8)]
        return pieces_in_col

    def get_pieces_in_row_list(self, row_number):
        # Given row_number return a list of pieces in that row.
        row_index = 8 - int(row_number)
        pieces_in_row = self.pieces[row_index]
        return pieces_in_row

    def get_pieces_by_rows_dict(self):
        # return a dict of the pieces in each row from left to right order.
        pieces_by_row = {}
        for row in range(8, 0, -1):
            pieces_by_row[row] = []
            for piece in self.pieces[8 - row]:
                pieces_by_row[row].append(piece.name)
        return pieces_by_row

    def get_pieces_by_cols_dict(self):
        # return a dict of the pieces in each col starting at row-8 going to row-1.
        pieces_by_col = {}
        for col in range(len(self.cols)):
            pieces_by_col[self.cols[col]] = []
            for row in range(8):
                pieces_by_col[self.cols[col]].append(self.pieces[row][col].name)
        return pieces_by_col

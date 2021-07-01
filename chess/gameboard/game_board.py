from chess.gameboard.square import Square
from chess.gameboard.empty_space import Empty_Space


class GameBoard:
    def __init__(self, pieces=[[Empty_Space() for _ in range(8)] for _ in range(8)]):
        # initilize a Game Board using a provided pieces array.
        # pieces defaults to an array of empty squares if no pieces are supplied
        self.columns = "ABCDEFGH"
        self.pieces = pieces

        self.board = []
        # set game board paints the squares, and places each piece on the board. 
        self.set_board(pieces)

    def update_game_board(self, player_move):
        if player_move["move_type"] == "move":
            # Calculate the indicies of the pieces array that need to be changed. 
            from_pieces_index_row = 8 - int(player_move["from"][1])
            from_pieces_index_col = self.columns.index(player_move["from"][0])
            to_pieces_index_row = 8 - int(player_move["to"][1])
            to_pieces_index_col = self.columns.index(player_move["to"][0])

            # Get the piece that needs to move, and update its position
            moving_piece = self.get_piece_at_position(player_move["from"])
            moving_piece.set_position(player_move["to"])
            
            # copy pieces arrary, and make necessary changes. 
            new_pieces_array = self.pieces[:]
            new_pieces_array[from_pieces_index_row][from_pieces_index_col] = Empty_Space()
            new_pieces_array[to_pieces_index_row][to_pieces_index_col] = moving_piece

            # call set_pieces, and set_board
            self.set_pieces(new_pieces_array)
            self.set_board(new_pieces_array)

    def set_pieces(self, updated_pieces): 
        self.pieces = updated_pieces
        
    def set_board(self, pieces): 
        # given a pieces array populate a GameBoard of Squares with the given pieces. 
        square_colors = { 0: "white", 1: "black", 2: "white" } # Dict used to apply color to square backgrounds
        board = []
        for row in range(8):
            current_row = []
            for col in range(8): 
                square_color =  square_colors[(col % 2) + (row % 2)]
                square_label = f"{self.columns[col]}{8 - row}"
                square_piece = pieces[row][col]
                current_row.append(Square(square_color, square_label, square_piece))
            board.append(current_row)
        self.board = board

    def get_piece_at_position(self, position):
        # Given poition in form '(ColumnLetter)(RowNumber)' return the piece object at that position
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
                temp_row = [x + y for x, y in zip(temp_row, rules[row_counter : row_counter + 3])]
                row_counter += 3
            display_board.append("\n".join(temp_row))

        return "\n".join(display_board) + "\n"

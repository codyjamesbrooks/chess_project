# Piece imports
from chess.gameboard.empty_space import Empty_Space
from chess.pieces.rook import Rook
from chess.pieces.bishop import Bishop
from chess.pieces.king import King
from chess.pieces.knight import Knight
from chess.pieces.pawn import Pawn
from chess.pieces.queen import Queen


test_board_strings = [
    # inital setup
    "RNBQKBNR PPPPPPPP 00000000 00000000 00000000 00000000 pppppppp rnbqkbnr",
    # mvmt_board_1
    "R00QB0RK PPB00P0P 00N0PpP0 b000n000 0rb0p00q 00p00r00 0p0000pp 0000000k",
    # mvmt_board_2
    "RNBQKBNR P00P00P0 00P00000 0P00PP00 00p0p000 0p0p0ppP p000000p rnbqkbnr",
    # mvmt_board_3
    "R0B0K000 N0P0p0Pp 0pPp0NB0 0000Qp0R 0P00p000 Pp000n00 PpP0P000 rnbqkb0r",
    # mvmt_board_4
    "00RR00K0 0P000PPP P000P000 0B000000 000b0p00 pp0qP0p0 0Qp0000p r00r00k0"
]

def populate_test_piece_array(test_board_string):
    # function will take a test board string with board rows seperated by spaces
    # It will return an 8 X 8 array of pieces that can be used to instinate a GameBoard
    test_piece_key = {
    "r": Rook,
    "b": Bishop,
    "n": Knight,
    "q": Queen,
    "k": King,
    "p": Pawn,  
    }

    test_board_string_rows = test_board_string.split(" ")
    test_pieces = []
    for row in range(8):
        test_pieces.append([])
        row_pieces = list(test_board_string_rows[row]) 
        row_str = str(8 - row)
        
        for col in range(8): 
            col_str = "ABCDEFGH"[col]
            position = f"{col_str}{row_str}"
            piece_letter = row_pieces[col]

            if piece_letter == "0": 
                test_pieces[row].append(Empty_Space())
            else: 
                piece_color = { True: "red", False: "blue" }[piece_letter.islower()]
                piece_class = test_piece_key[piece_letter.lower()]
                test_pieces[row].append(piece_class(piece_color, position))
    return test_pieces

# The test files will all import their test piece arrays from the test_boards array. 
test_boards = [populate_test_piece_array(board_string) for board_string in test_board_strings]


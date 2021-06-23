# Piece imports
from chess.gameboard.empty_space import Empty_Space
from chess.pieces.rook import Rook
from chess.pieces.bishop import Bishop
from chess.pieces.king import King
from chess.pieces.knight import Knight
from chess.pieces.pawn import Pawn
from chess.pieces.queen import Queen

test_boards = [
    # Just Blues
    "RNBQKBNR PPPPPPPP 00000000 00000000 00000000 00000000 00000000 00000000",
    # Just Reds
    "00000000 00000000 00000000 00000000 00000000 00000000 pppppppp rnbqkbnr",
    # inital setup
    "RNBQKBNR PPPPPPPP 00000000 00000000 00000000 00000000 pppppppp rnbqkbnr",
    # setup one
    "R00QB0RK PPB00P0P 00N0PpP0 b000n000 00b0p00q 00p00r00 0p0000pp 0000000k",
]

test_boards_key = [
    [],  # Just Blues, No Key needed
    [],  # Just Reds, No Key needed
    [],  # Inital Setup, No key needed
    # Key for setup one
    [[Rook("blue"), Empty_Space(), Empty_Space(), Queen("blue"), Bishop("blue"), Empty_Space(), Rook("blue"), King("blue")],
     [Pawn("blue"), Pawn("blue"), Bishop("blue"), Empty_Space(), Empty_Space(), Pawn("blue"), Empty_Space(), Pawn("blue")],
     [Empty_Space(), Empty_Space(), Knight("blue"), Empty_Space(), Pawn("blue"), Pawn("red"), Pawn("blue"), Empty_Space()],
     [Bishop("red"), Empty_Space(), Empty_Space(), Empty_Space(), Knight("red"), Empty_Space(), Empty_Space(), Empty_Space()],
     [Empty_Space(), Empty_Space(), Bishop("red"), Empty_Space(), Pawn("red"), Empty_Space(), Empty_Space(), Queen("red")],
     [Empty_Space(), Empty_Space(), Pawn("red"), Empty_Space(), Empty_Space(), Rook("red"), Empty_Space(), Empty_Space()],
     [Empty_Space(), Pawn("red"), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Pawn("red"), Pawn("red")],
     [Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), King("red")]]
]

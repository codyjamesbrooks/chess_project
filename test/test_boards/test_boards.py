# Piece imports
from chess.gameboard.empty_space import Empty_Space
from chess.pieces.rook import Rook
from chess.pieces.bishop import Bishop
from chess.pieces.king import King
from chess.pieces.knight import Knight
from chess.pieces.pawn import Pawn
from chess.pieces.queen import Queen

test_boards = [
    # inital setup
    "RNBQKBNR PPPPPPPP 00000000 00000000 00000000 00000000 pppppppp rnbqkbnr",
    # setup one
    "R00QB0RK PPB00P0P 00N0PpP0 b000n000 00b0p00q 00p00r00 0p0000pp 0000000k",
]

test_boards_key = [
    [],  # Inital Setup No Key needed
    # Key for setup one
    [[Rook("blue", "A8"), Empty_Space(), Empty_Space(), Queen("blue", "D8"), Bishop("blue", "E8"), Empty_Space(), Rook("blue", "G8"), King("blue", "H8")],
     [Pawn("blue", "A7"), Pawn("blue", "B7"), Bishop("blue", "C7"), Empty_Space(), Empty_Space(), Pawn("blue", "F7"), Empty_Space(), Pawn("blue", "H7")],
     [Empty_Space(), Empty_Space(), Knight("blue", "C6"), Empty_Space(), Pawn("blue", "E6"), Pawn("red", "F6"), Pawn("blue", "G6"), Empty_Space()],
     [Bishop("red", "A5"), Empty_Space(), Empty_Space(), Empty_Space(), Knight("red", "E5"), Empty_Space(), Empty_Space(), Empty_Space()],
     [Empty_Space(), Empty_Space(), Bishop("red", "C4"), Empty_Space(), Pawn("red", "E4"), Empty_Space(), Empty_Space(), Queen("red", "H4")],
     [Empty_Space(), Empty_Space(), Pawn("red", "C3"), Empty_Space(), Empty_Space(), Rook("red", "F3"), Empty_Space(), Empty_Space()],
     [Empty_Space(), Pawn("red", "B2"), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Pawn("red", "G2"), Pawn("red", "H2")],
     [Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), Empty_Space(), King("red", "H1")]]
]

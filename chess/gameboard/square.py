from colorama import Fore, Back, Style
from chess.gameboard.empty_space import Empty_Space


class Square:
    def __init__(self, square_color, cornor_label, piece):
        # Each Square will have a background color, a label (that will be displayed in the upper lh cornor),
        # and final parameter that will be used to display a chess piece that is sitting on that square
        self.square_color = square_color
        self.cornor_label = cornor_label
        self.piece = piece
        self.piece_label = self.color_in_piece(piece)

    def __repr__(self):
        square_string = self.assemble_square()
        return "\n".join(square_string)

    def assemble_square(self):
        # Return an array of strings that when will represent a single square on a chess board
        # Each square will be a 3 row string that has the following layout
        square_array = [f"{self.color_in_label(self.cornor_label)}     ",
                        f"  {self.piece_label}   ",
                        "       "]
        square_array = self.color_in_background(square_array)
        return square_array

    def color_in_label(self, cornor_label):
        return Style.DIM + Fore.GREEN + cornor_label

    def color_in_piece(self, piece):
        piece_color = {"red": Fore.RED, "blue": Fore.BLUE, None: ""}
        return piece_color[piece.color] + Style.BRIGHT + piece.alias.rjust(2, " ")

    def color_in_background(self, square_array):
        back_color = {"white": Back.WHITE, "black": Back.BLACK}
        colored_square = [back_color[self.square_color] + row + Style.RESET_ALL for row in square_array]
        return colored_square

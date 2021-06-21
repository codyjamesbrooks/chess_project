from colorama import init, Fore, Back, Style 

class Square: 
    def __init__(self, square_color, cornor_label, piece):
        # Each Square will have a background color, a label (that will be displayed in the upper lh cornor), 
        # and an optional parameter that will be used to display a chess piece that is sitting on that square
        self.square_color = square_color
        self.cornor_label = Style.DIM + apply_foreground_color("green", cornor_label)
        self.piece = piece
        self.piece_label = Style.BRIGHT + apply_foreground_color(piece.color, piece.alias.rjust(2, " "))
        
    def __repr__(self):
        square_string = self.assemble_square()
        return "\n".join(square_string)
        
    def assemble_square(self): 
        # Return an array of strings that when will represent a single square on a chess board
        # Each square will be a 3 row string that has the following layout
        square_array = [f"{self.cornor_label}     ",  
                        f"  {self.piece_label}   ",
                        "       "]
        
        # Apply a background color to the square, and then Reset any lingering style settings
        square_array = [apply_background_color(self.square_color, row) + Style.RESET_ALL for row in square_array]
   
        return square_array
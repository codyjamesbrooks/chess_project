class Piece:
    def __init__(self, color, position=None):
        self.name = None
        self.color = color
        self.position = position
        self.columns = "ABCDEFGH"  # Used for indexing and finding potential moves

    def __repr__(self):
        return f"{self.color.title()} {self.name}"

    def __eq__(self, other): 
        return ( self.name == other.name and
                 self.color == other.color and
                 self.position == self.position )

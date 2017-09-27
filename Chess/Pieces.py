class Piece:
    def __init__(self, name, diag, horiverti): #does not include pawns or knights
        self.name = name
        self.diag = diag           #move diagonally?
        self.horiverti = horiverti #horizontally or vertically?
King = Piece('Ki', 'y', 'y')
Queen = Piece('Qu', 'y', 'y')
Bishop = Piece('Bi', 'y', 'n')
Rook = Piece('Ro', 'n', 'y')

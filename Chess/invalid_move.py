'''need to improve invalid move function'''
from Pieces import Piece

def invalid_move(board, colour_from, colour_to, c):
    key = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    if colour_from[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']\
    and colour_from[1] in str(range(1, 9)):
        f1 = str(board[9-int(colour_from[1])][key[colour_from[0]]])
    else:
        f1 = str(0)

    if f1[0] == c\
    and len(f1) == 2\
    and (colour_from[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])\
    and (int(colour_to[1]) in range(1, 9))\
    and (colour_to[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])\
    and (int(colour_from[1]) in range(1, 9)):
        return False        #valid move

    else:
        return True         #invalid move

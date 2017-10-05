from coord import coord

def invalid_move(board, colour_from, colour_to, c, log):
    if len(colour_from) != 2:
        colour_from = 'z0'
    if len(colour_to) != 2:
        colour_to = 'z0'
    #key = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    if colour_from[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']\
    and colour_from[1] in str(range(1, 9)):
        piece = str(board[int(coord(colour_from)[0])][int(coord(colour_from)[1])])
    else:
        piece = str(0)
    if piece[0] == c\
    and (colour_from[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])\
    and (int(colour_to[1]) in range(1, 9))\
    and (colour_to[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])\
    and (int(colour_from[1]) in range(1, 9))\
    and board[int(coord(colour_to)[0])][int(coord(colour_to)[1])][0] != str(c)\
    and colour_from != colour_to:
        if piece == 'bPa': #if black pawn
            if int(colour_from[1]) == 7: #first move
                if (int(colour_from[1]) - int(colour_to[1]) == 1\
                and colour_from[0] == colour_to[0]\
                and board[int(coord(colour_to)[0])][int(coord(colour_to)[1])][0] != 'w')\
                or (int(colour_from[1]) - int(colour_to[1]) == 2\
                and colour_from[0] == colour_to[0]\
                and board[int(coord(colour_to)[0])][int(coord(colour_to)[1])][0] != 'w'\
                and ((board[int(coord(colour_to)[0])-1][int(coord(colour_to)[1])]) == ' W ' or (board[int(coord(colour_to)[0])-1][int(coord(colour_to)[1])]) == ' B '))\
                or ((int(colour_from[1]) - int(colour_to[1]) == 1\
                and abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1])) == 1)\
                and board[int(coord(colour_to)[0])][int(coord(colour_to)[1])][0] == 'w'):
                #move one if empty or move two if both empty or take diagonally if not empty
                    return False
                else:
                    return True
            else:
                if (int(colour_from[1]) - int(colour_to[1]) == 1\
                and colour_from[0] == colour_to[0]\
                and board[int(coord(colour_to)[0])][int(coord(colour_to)[1])][0] != 'w')\
                or ((int(colour_from[1]) - int(colour_to[1]) == 1\
                and abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1])) == 1)\
                and board[int(coord(colour_to)[0])][int(coord(colour_to)[1])][0] == 'w')\
                or (log[-1][0] == 'wPa'\
                and int(log[-1][1][1]) - int(log[-1][2][1]) == -2\
                and int(colour_from[1]) - int(colour_to[1]) == 1\
                and abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1])) == 1\
                and board[int(coord(colour_to)[0]) - 1][int(coord(colour_to)[1])][0] == 'w'):
                    return False #else move one if empty or move diagonally if not empty or en passant
                else:
                    return True
        if piece == 'wPa': #if white pawn
            if int(colour_from[1]) == 2: #first move
                if (int(colour_from[1]) - int(colour_to[1]) == -1\
                and colour_from[0] == colour_to[0]\
                and board[int(coord(colour_to)[0])][int(coord(colour_to)[1])][0] != 'b')\
                or (int(colour_from[1]) - int(colour_to[1]) == -2\
                and colour_from[0] == colour_to[0]\
                and board[int(coord(colour_to)[0])][int(coord(colour_to)[1])][0] != 'b'\
                and (board[int(coord(colour_to)[0]) + 1][int(coord(colour_to)[1])] == ' W ' or board[int(coord(colour_to)[0]) + 1][int(coord(colour_to)[1])] == ' B '))\
                or (int(colour_from[1]) - int(colour_to[1]) == -1\
                and abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1])) == 1\
                and board[int(coord(colour_to)[0])][int(coord(colour_to)[1])][0] == 'b'):
                #move one if empty or move two if both empty or take diagonally if not empty
                    return False
                else:
                    return True
            else:
                if (int(colour_from[1]) - int(colour_to[1]) == -1\
                and colour_from[0] == colour_to[0]\
                and board[int(coord(colour_to)[0])][int(coord(colour_to)[1])][0] != 'b')\
                or (int(colour_from[1]) - int(colour_to[1]) == -1\
                and abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1])) == 1\
                and board[int(coord(colour_to)[0])][int(coord(colour_to)[1])][0] == 'b')\
                or (log[-1][0] == 'bPa'\
                and int(log[-1][1][1]) - int(log[-1][2][1]) == 2\
                and int(colour_from[1]) - int(colour_to[1]) == -1\
                and abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1])) == 1\
                and board[int(coord(colour_to)[0]) + 1][int(coord(colour_to)[1])][0] == 'b'):
                    return False #else move one if empty or move diagonally if not empty or en passant
                else:
                    return True
        if piece == 'wKi' or piece == 'bKi': #if king
            if (abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1])) == 1\
            and coord(colour_from)[0] == coord(colour_to)[0])\
            or (coord(colour_from)[1] == coord(colour_to)[1]\
            and abs(int(coord(colour_to)[0]) - int(coord(colour_from)[0])) == 1)\
            or (abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1])) == 1\
            and abs(int(coord(colour_to)[0]) - int(coord(colour_from)[0])) == 1):
            #single space vertical movement or horizontal movement or diagonal movement
                return False
            elif piece == 'bKi'\
            and 'bKi' not in ''.join(reduce(lambda x,y: x+y,log))\
            and 'bRoa8' not in ''.join(reduce(lambda x,y: x+y,log))\
            and board[int(coord('b8')[0])][int(coord('b8')[1])] == ' B '\
            and board[int(coord('c8')[0])][int(coord('c8')[1])] == ' W '\
            and board[int(coord('d8')[0])][int(coord('d8')[1])] == ' B '\
            and colour_to == 'c8': #black castle left
                return False
            elif piece == 'bKi'\
            and 'bKi' not in ''.join(reduce(lambda x,y: x+y,log))\
            and 'bRoh8' not in ''.join(reduce(lambda x,y: x+y,log))\
            and board[int(coord('f8')[0])][int(coord('f8')[1])] == ' B '\
            and board[int(coord('g8')[0])][int(coord('g8')[1])] == ' W '\
            and colour_to == 'g8': #black castle right
                return False
            elif piece == 'wKi'\
            and 'wKi' not in ''.join(reduce(lambda x,y: x+y,log))\
            and 'wRoa1' not in ''.join(reduce(lambda x,y: x+y,log))\
            and board[int(coord('b1')[0])][int(coord('b1')[1])] == ' W '\
            and board[int(coord('c1')[0])][int(coord('c1')[1])] == ' B '\
            and board[int(coord('d1')[0])][int(coord('d1')[1])] == ' W '\
            and colour_to == 'c1': #white castle left
                return False
            elif piece == 'wKi'\
            and 'wKi' not in ''.join(reduce(lambda x,y: x+y,log))\
            and 'wRoh1' not in ''.join(reduce(lambda x,y: x+y,log))\
            and board[int(coord('f1')[0])][int(coord('f1')[1])] == ' W '\
            and board[int(coord('g1')[0])][int(coord('g1')[1])] == ' B '\
            and colour_to == 'g1': #white castle right
                return False
            else:
                return True
        if piece == 'wKn' or piece == 'bKn': #if knight
            if (abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1])) == 1\
            and abs(int(coord(colour_to)[0]) - int(coord(colour_from)[0])) == 2)\
            or (abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1])) == 2\
            and abs(int(coord(colour_to)[0]) - int(coord(colour_from)[0])) == 1):
                return False
            else:
                return True
        if piece == 'wRo' or piece == 'bRo': #if rook
            if abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1])) in range(1, 9)\
            and coord(colour_from)[0] == coord(colour_to)[0]:
                clear = 0
                sign1 = (int(coord(colour_from)[1])-int(coord(colour_to)[1]))/abs(int(coord(colour_from)[1])-int(coord(colour_to)[1]))
                for i in range(1, abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1]))):
                    if board[int(coord(colour_from)[0])][int(coord(colour_from)[1])-i*sign1] == ' W '\
                    or board[int(coord(colour_from)[0])][int(coord(colour_from)[1])-i*sign1] == ' B ':
                        clear += 1
                if clear == abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1])) - 1:
                    return False
                else:
                    return True
            elif coord(colour_from)[1] == coord(colour_to)[1]\
            and abs(int(coord(colour_to)[0])-int(coord(colour_from)[0])) in range(1, 9):
                clear = 0
                sign0 = (int(coord(colour_from)[0])-int(coord(colour_to)[0]))/abs(int(coord(colour_from)[0])-int(coord(colour_to)[0]))
                for i in range(1, abs(int(coord(colour_from)[0]) - int(coord(colour_to)[0]))):
                    if board[int(coord(colour_from)[0])-i*sign0][int(coord(colour_from)[1])] == ' W '\
                    or board[int(coord(colour_from)[0])-i*sign0][int(coord(colour_from)[1])] == ' B ':
                        clear += 1
                if clear == abs(int(coord(colour_from)[0]) - int(coord(colour_to)[0])) - 1:
                    return False
                else:
                    return True
            else:
                return True
        if piece == 'wBi' or piece == 'bBi': #if bishop
            if abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1]))\
            == abs(int(coord(colour_from)[0]) - int(coord(colour_to)[0])):
                clear = 0
                sign0 = (int(coord(colour_from)[0])-int(coord(colour_to)[0]))/abs(int(coord(colour_from)[0])-int(coord(colour_to)[0]))
                sign1 = (int(coord(colour_from)[1])-int(coord(colour_to)[1]))/abs(int(coord(colour_from)[1])-int(coord(colour_to)[1]))
                for i in range(1, abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1]))):
                    if board[int(coord(colour_from)[0])-i*sign0][int(coord(colour_from)[1])-i*sign1] == ' W '\
                    or board[int(coord(colour_from)[0])-i*sign0][int(coord(colour_from)[1])-i*sign1] == ' B ':
                        clear += 1
                if clear == abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1])) - 1:
                    return False
                else:
                    return True
            else:
                return True
        if piece == 'wQu' or piece == 'bQu': #if queen
            if abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1])) in range(1, 9)\
            and coord(colour_from)[0] == coord(colour_to)[0]:
                clear = 0
                sign1 = (int(coord(colour_from)[1])-int(coord(colour_to)[1]))/abs(int(coord(colour_from)[1])-int(coord(colour_to)[1]))
                for i in range(1, abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1]))):
                    if board[int(coord(colour_from)[0])][int(coord(colour_from)[1])-i*sign1] == ' W '\
                    or board[int(coord(colour_from)[0])][int(coord(colour_from)[1])-i*sign1] == ' B ':
                        clear += 1
                if clear == abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1])) - 1:
                    return False
                else:
                    return True
            elif coord(colour_from)[1] == coord(colour_to)[1]\
            and abs(int(coord(colour_to)[0])-int(coord(colour_from)[0])) in range(1, 9):
                clear = 0
                sign0 = (int(coord(colour_from)[0])-int(coord(colour_to)[0]))/abs(int(coord(colour_from)[0])-int(coord(colour_to)[0]))
                for i in range(1, abs(int(coord(colour_from)[0]) - int(coord(colour_to)[0]))):
                    if board[int(coord(colour_from)[0])-i*sign0][int(coord(colour_from)[1])] == ' W '\
                    or board[int(coord(colour_from)[0])-i*sign0][int(coord(colour_from)[1])] == ' B ':
                        clear += 1
                if clear == abs(int(coord(colour_from)[0]) - int(coord(colour_to)[0])) - 1:
                    return False
                else:
                    return True
            elif abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1]))\
            == abs(int(coord(colour_to)[0]) - int(coord(colour_from)[0])):
                clear = 0
                sign0 = (int(coord(colour_from)[0])-int(coord(colour_to)[0]))/abs(int(coord(colour_from)[0])-int(coord(colour_to)[0]))
                sign1 = (int(coord(colour_from)[1])-int(coord(colour_to)[1]))/abs(int(coord(colour_from)[1])-int(coord(colour_to)[1]))
                for i in range(1, abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1]))):
                    if board[int(coord(colour_from)[0])-i*sign0][int(coord(colour_from)[1])-i*sign1] == ' W '\
                    or board[int(coord(colour_from)[0])-i*sign0][int(coord(colour_from)[1])-i*sign1] == ' B ':
                        clear += 1
                if clear == abs(int(coord(colour_from)[1]) - int(coord(colour_to)[1])) - 1:
                    return False
                else:
                    return True
            else:
                return True
    else:
        return True #invalid move

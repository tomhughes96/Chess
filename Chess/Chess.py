'''Type moves in format 'a1' and type 'forfeit' to quit'''

from invalid_move import invalid_move
from coord import coord

Board = (
    [' ', ' a ', ' b ', ' c ', ' d ', ' e ', ' f ', ' g ', ' h '],
    ['8', ' W ', ' B ', ' W ', ' B ', ' W ', ' B ', ' W ', ' B '],
    ['7', ' B ', ' W ', ' B ', ' W ', ' B ', ' W ', ' B ', ' W '],
    ['6', ' W ', ' B ', ' W ', ' B ', ' W ', ' B ', ' W ', ' B '],
    ['5', ' B ', ' W ', ' B ', ' W ', ' B ', ' W ', ' B ', ' W '],
    ['4', ' W ', ' B ', ' W ', ' B ', ' W ', ' B ', ' W ', ' B '],
    ['3', ' B ', ' W ', ' B ', ' W ', ' B ', ' W ', ' B ', ' W '],
    ['2', ' W ', ' B ', ' W ', ' B ', ' W ', ' B ', ' W ', ' B '],
    ['1', ' B ', ' W ', ' B ', ' W ', ' B ', ' W ', ' B ', ' W ']
)
Board[1][1] = 'bRo'
Board[1][2] = 'bKn'
Board[1][3] = 'bBi'
Board[1][4] = 'bQu'
Board[1][5] = 'bKi'
Board[1][6] = 'bBi'
Board[1][7] = 'bKn'
Board[1][8] = 'bRo'
Board[8][1] = 'wRo'
Board[8][2] = 'wKn'
Board[8][3] = 'wBi'
Board[8][4] = 'wQu'
Board[8][5] = 'wKi'
Board[8][6] = 'wBi'
Board[8][7] = 'wKn'
Board[8][8] = 'wRo'
for j in range(1, 9):
    Board[2][j] = 'bPa'
for j in range(1, 9):
    Board[7][j] = 'wPa'
for x in Board:
    print x                                     #initial board set up
key = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
log = []
while any("bKi" in x for x in Board)\
and any("wKi" in x for x in Board):             #while the kings are alive
    white_from = raw_input('white move from:')  #ask for move from white
    white_to = raw_input('to:')
    while invalid_move(Board, white_from, white_to, 'w', log):
        if white_from == 'forfeit' or white_to == 'forfeit':
            Board = 'forfeit'
            break
        white_from = raw_input('white please choose valid move from:')  #ask again
        white_to = raw_input('to:')
    else:
        Board[int(coord(white_to)[0])][int(coord(white_to)[1])]\
        = Board[int(coord(white_from)[0])][int(coord(white_from)[1])]
        if white_to[1] == '8'\
        and Board[int(coord(white_from)[0])][int(coord(white_from)[1])] == 'wPa':
            Board[int(coord(white_to)[0])][int(coord(white_to)[1])] = 'wQu' #queening condition
        if len(log) > 0\
        and log[-1][0] == 'bPa'\
        and Board[int(coord(white_from)[0])][int(coord(white_from)[1])] == 'wPa'\
        and int(log[-1][1][1]) - int(log[-1][2][1]) == 2\
        and int(white_from[1]) - int(white_to[1]) == -1\
        and abs(int(coord(white_from)[1]) - int(coord(white_to)[1])) == 1\
        and Board[int(coord(white_to)[0]) + 1][int(coord(white_to)[1])][0] == 'b': #en passant
            if (key[white_from[0]]+int(white_from[1]))%2 == 0:
                Board[int(coord(white_to)[0])+1][int(coord(white_to)[1])] = ' W '
            else:
                Board[int(coord(white_to)[0])+1][int(coord(white_to)[1])] = ' B '
        if white_from == 'e1'\
        and 'wKi' not in ''.join(reduce(lambda x, y: x+y, log))\
        and 'wRoa1' not in ''.join(reduce(lambda x, y: x+y, log))\
        and Board[int(coord('b1')[0])][int(coord('b1')[1])] == ' W '\
        and Board[int(coord('d1')[0])][int(coord('d1')[1])] == ' W '\
        and white_to == 'c1': #castle left
            Board[int(coord('d1')[0])][int(coord('d1')[1])] = 'wRo'
            Board[int(coord('a1')[0])][int(coord('a1')[1])] = ' B '
        if white_from == 'e1'\
        and 'wKi' not in ''.join(reduce(lambda x, y: x+y, log))\
        and 'wRoh1' not in ''.join(reduce(lambda x, y: x+y, log))\
        and Board[int(coord('f1')[0])][int(coord('f1')[1])] == ' W '\
        and white_to == 'g1': #castle right
            Board[int(coord('f1')[0])][int(coord('f1')[1])] = 'wRo'
            Board[int(coord('h1')[0])][int(coord('h1')[1])] = ' W '
        if (key[white_from[0]]+int(white_from[1]))%2 == 1:
            Board[int(coord(white_from)[0])][int(coord(white_from)[1])] = ' W '
        else:
            Board[int(coord(white_from)[0])][int(coord(white_from)[1])] = ' B '
        log.append([Board[int(coord(white_to)[0])][int(coord(white_to)[1])], white_from, white_to])
        print log
    for x in Board:
        print x                                 #end white's turn and print board

    if any("bKi" in x for x in Board):          #if black king still alive
        black_from = raw_input('black move from:')
        black_to = raw_input('to:')
        while invalid_move(Board, black_from, black_to, 'b', log):
            if black_from == 'forfeit' or black_to == 'forfeit':
                Board = 'forfeit'
                break
            black_from = raw_input('black please choose valid move from:')  #ask again
            black_to = raw_input('to:')
        else:
            Board[int(coord(black_to)[0])][int(coord(black_to)[1])]\
            = Board[int(coord(black_from)[0])][int(coord(black_from)[1])]
            if black_to[1] == '1'\
            and Board[int(coord(black_from)[0])][int(coord(black_from)[1])] == 'bPa':
                Board[int(coord(black_to)[0])][int(coord(black_to)[1])] = 'bQu' #queening condition
            if len(log) > 0\
            and Board[int(coord(black_from)[0])][int(coord(black_from)[1])] == 'bPa'\
            and log[-1][0] == 'wPa'\
            and int(log[-1][1][1]) - int(log[-1][2][1]) == -2\
            and int(black_from[1]) - int(black_to[1]) == 1\
            and abs(int(coord(black_from)[1]) - int(coord(black_to)[1])) == 1\
            and Board[int(coord(black_to)[0]) - 1][int(coord(black_to)[1])][0] == 'w': #en passant
                if (key[black_from[0]]+int(black_from[1]))%2 == 0:
                    Board[int(coord(black_to)[0])-1][int(coord(black_to)[1])] = ' W '
                else:
                    Board[int(coord(black_to)[0])-1][int(coord(black_to)[1])] = ' B '
            if black_from == 'e8'\
            and 'bKi' not in ''.join(reduce(lambda x, y: x+y, log))\
            and 'bRoa8' not in ''.join(reduce(lambda x, y: x+y, log))\
            and Board[int(coord('b8')[0])][int(coord('b8')[1])] == ' B '\
            and Board[int(coord('d8')[0])][int(coord('d8')[1])] == ' B '\
            and black_to == 'c8': #castle right
                Board[int(coord('d8')[0])][int(coord('d8')[1])] = 'bRo'
                Board[int(coord('a8')[0])][int(coord('a8')[1])] = ' W '
            if black_from == 'e8'\
            and 'bKi' not in ''.join(reduce(lambda x, y: x+y, log))\
            and 'bRoh8' not in ''.join(reduce(lambda x, y: x+y, log))\
            and Board[int(coord('f8')[0])][int(coord('f8')[1])] == ' B '\
            and black_to == 'g8': #castle left
                Board[int(coord('f8')[0])][int(coord('f8')[1])] = 'bRo'
                Board[int(coord('h8')[0])][int(coord('h8')[1])] = ' B '
            if (key[black_from[0]]+int(black_from[1]))%2 == 1:
                Board[int(coord(black_from)[0])][int(coord(black_from)[1])] = ' W '
            else:
                Board[int(coord(black_from)[0])][int(coord(black_from)[1])] = ' B '
            log.append([Board[int(coord(black_to)[0])][int(coord(black_to)[1])], black_from, black_to])
            print log
        for x in Board:
            print x                               #end white's turn and print board
print 'Game Over'
if len(log) % 2 == 0:
    print 'Black Wins In %s Turns' % str((len(log))/2)
else:
    print 'White Wins In %s Turns' % str((len(log)+1)/2)

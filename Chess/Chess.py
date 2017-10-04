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
        log.append([Board[int(coord(white_from)[0])][int(coord(white_from)[1])], white_from, white_to])
        print log
        if white_to[1] == '8'\
        and Board[int(coord(white_from)[0])][int(coord(white_from)[1])] == 'wPa':
            Board[int(coord(white_to)[0])][int(coord(white_to)[1])] = 'wQu' #queening condition
#        if log[-2][0] == 'bPa'\
#        and int(log[-2][1][1]) - int(log[-2][2][1]) == 2\
#        and int(white_from[1]) - int(white_to[1]) == -1\
#        and abs(int(coord(white_from)[1]) - int(coord(white_to)[1])) == 1\
#        and Board[int(coord(white_to)[0]) + 1][int(coord(white_to)[1])][0] == 'b':
#            if (key[white_from[0]]+int(white_from[1]))%2 == 0:
#                Board[int(coord(white_from)[0])-1][int(coord(white_from)[1])] = ' W '
#            else:
#                Board[int(coord(white_from)[0])-1][int(coord(white_from)[1])] = ' B '
        if (key[white_from[0]]+int(white_from[1]))%2 == 1:
            Board[int(coord(white_from)[0])][int(coord(white_from)[1])] = ' W '
        else:
            Board[int(coord(white_from)[0])][int(coord(white_from)[1])] = ' B '
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
            log.append([Board[int(coord(black_from)[0])][int(coord(black_from)[1])], black_from, black_to])
            print log
            if black_to[1] == '1'\
            and Board[int(coord(black_from)[0])][int(coord(black_from)[1])] == 'bPa':
                Board[int(coord(black_to)[0])][int(coord(black_to)[1])] = 'bQu' #queening condition
#            if log[-2][0] == 'wPa'\
#            and int(log[-2][1][1]) - int(log[-2][2][1]) == -2\
#            and int(black_from[1]) - int(black_to[1]) == 1\
#            and abs(int(coord(black_from)[1]) - int(coord(black_to)[1])) == 1\
#            and Board[int(coord(black_to)[0]) - 1][int(coord(black_to)[1])][0] == 'w':
#                if (key[black_from[0]]+int(black_from[1]))%2 == 0:
#                    Board[int(coord(black_from)[0])-1][int(coord(black_from)[1])] = ' W '
#                else:
#                    Board[int(coord(black_from)[0])-1][int(coord(black_from)[1])] = ' B '
            if (key[black_from[0]]+int(black_from[1]))%2 == 1:
                Board[int(coord(black_from)[0])][int(coord(black_from)[1])] = ' W '
            else:
                Board[int(coord(black_from)[0])][int(coord(black_from)[1])] = ' B '
        for x in Board:
            print x                               #end white's turn and print board
print 'Game Over'
if len(log) % 2 == 0:
    print 'Black Wins In %s Turns' % str((len(log))/2)
else:
    print 'White Wins In %s Turns' % str((len(log)+1)/2)

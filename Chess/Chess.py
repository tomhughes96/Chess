from invalid_move import invalid_move


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
Board[1][1] = 'bKn'
Board[1][2] = 'bRo'
Board[1][3] = 'bBi'
Board[1][4] = 'bQu'
Board[1][5] = 'bKi'
Board[1][6] = 'bBi'
Board[1][7] = 'bRo'
Board[1][8] = 'bKn'
Board[8][1] = 'wKn'
Board[8][2] = 'wRo'
Board[8][3] = 'wBi'
Board[8][4] = 'wQu'
Board[8][5] = 'wKi'
Board[8][6] = 'wBi'
Board[8][7] = 'wRo'
Board[8][8] = 'wKn'
for j in range(1, 9):
    Board[2][j] = 'bPa'
for j in range(1, 9):
    Board[7][j] = 'wPa'
for x in Board:
    print x                                     #initial board set up
key = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
w = 0
b = 0

while any("bKi" in x for x in Board)\
and any("wKi" in x for x in Board):             #while the kings are alive
    white_from = raw_input('white move from:')  #ask for move from white
    white_to = raw_input('to:')
    while invalid_move(Board, white_from, white_to, 'w'):
        if white_from == 'forfeit' or white_to == 'forfeit':
            Board = 'forfeit'
            b = w + 1
            break
        white_from = raw_input('white please choose valid move from:')  #ask again
        white_to = raw_input('to:')
    else:
        Board[9-int(white_to[1])][key[white_to[0]]]\
        = Board[9-int(white_from[1])][key[white_from[0]]]
        if (key[white_from[0]]+int(white_from[1]))%2 == 1:
            Board[9-int(white_from[1])][key[white_from[0]]] = ' W '
        else:
            Board[9-int(white_from[1])][key[white_from[0]]] = ' B '
    for x in Board:
        print x                                 #end white's turn and print board
    w += 1

    if any("bKi" in x for x in Board):          #if black king still alive
        black_from = raw_input('black move from:')
        black_to = raw_input('to:')
        while invalid_move(Board, black_from, black_to, 'b'):
            if black_from == 'forfeit' or black_to == 'forfeit':
                Board = 'forfeit'
                b = w
                break
            black_from = raw_input('black please choose valid move from:')  #ask again
            black_to = raw_input('to:')
        else:
            Board[9-int(black_to[1])][key[black_to[0]]]\
            = Board[9-int(black_from[1])][key[black_from[0]]]
            if (key[black_from[0]]+int(black_from[1]))%2 == 1:
                Board[9-int(black_from[1])][key[black_from[0]]] = ' W '
            else:
                Board[9-int(black_from[1])][key[black_from[0]]] = ' B '
        for x in Board:
            print x                               #end white's turn and print board
        b += 1
print 'Game Over'
if w == b:
    print 'Black Wins In %d Turns' % w
else:
    print 'White Wins In %d Turns' % w

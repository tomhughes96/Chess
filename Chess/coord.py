def coord(entry):
    key = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    return str(9-int(entry[1])) + str(key[entry[0]]) #board coordinates

# str(board[int(coord(entry)[0])][int(coord(entry)[1])]) is the Piece in entry

from string import ascii_lowercase

def validate(rook_position):
    if  rook_position[0] in (ascii_lowercase[0:8]) and int(rook_position[1]) in range(1,9):
        return True
    else:
        return 'Your rook is not on the board. Try again.'

def rook_moves(rook_position):
    moves = []
    for i in range(1,9):
        if i != int(rook_position[1]):
            moves.append(rook_position[0]+str(i))
    for j in ascii_lowercase[0:8]:
        if j != rook_position[0]:
            moves.append(j+rook_position[1])
    return moves

def display_moves(rook_moves_list):
    # to do
    return

def main():
    print ('Input rook position:')
    rook_position = input()
    if validate(rook_position) == True:
        rook_moves_list = rook_moves(rook_position)
        print (rook_moves_list)
    else: print(validate(rook_position))
    # display_moves(rook_moves_list)

if __name__ == "__main__":
    main()

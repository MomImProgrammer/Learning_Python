from string import ascii_lowercase

def validate(position):
    if  position[0] in ('Q','R','B'):
        if position[1] in (ascii_lowercase[0:8]) and int(position[2]) in range(1,9):
            return ''
        else:
            return 'Your piece is not on the board. Try again.'
    else:
        return 'Position must start with \'Q\', \'R\', \'B\'. Try again.'

def rook_moves(rook_position):
    moves = []
    for i in range(1,9):
        if i != int(rook_position[1]):
            moves.append(rook_position[0]+str(i))
    for j in ascii_lowercase[0:8]:
        if j != rook_position[0]:
            moves.append(j+rook_position[1])
    return moves

def bishop_moves(bishop_position):
    moves = []
    horiz_index = ascii_lowercase[0:8].index(bishop_position[0])    
    for i in range(1,8):        
        if horiz_index+i in range(0, 8) and int(bishop_position[1])+i in range(1, 9):
            moves.append(ascii_lowercase[horiz_index+i]+str(int(bishop_position[1])+i))
        if horiz_index-i in range(0, 8) and int(bishop_position[1])+i in range(1, 9):
            moves.append(ascii_lowercase[horiz_index-i]+str(int(bishop_position[1])+i))
        if horiz_index+i in range(0, 8) and int(bishop_position[1])-i in range(1, 9):
            moves.append(ascii_lowercase[horiz_index+i]+str(int(bishop_position[1])-i))
        if horiz_index-i in range(0, 8) and int(bishop_position[1])-i in range(1, 9):
            moves.append(ascii_lowercase[horiz_index-i]+str(int(bishop_position[1])-i))
    return moves

def display_moves(position, moves_list):
    for i in range(8,0,-1):
        for j in (ascii_lowercase[0:8]):
            cell = j+str(i)
            if cell == position:
                print('o', end='')
            elif cell in moves_list:
                print('x', end='')
            else:
                print('.', end='')
            if j == ascii_lowercase[7]:
                print('\n', end='')
    return

def main():
    print('Input queen or rook or bishop position(e.g. Qa7):')
    position = input()
    validation_error = validate(position)
    if  validation_error == '':
        if position[0] == 'B':
            moves_list = bishop_moves(position[1:3])
        elif position[0] == 'R':
            moves_list = rook_moves(position[1:3])
        elif position[0] == 'Q':
            moves_list = rook_moves(position[1:3])+bishop_moves(position[1:3])
        print (moves_list)
        display_moves(position[1:3], moves_list)
    else: print(validation_error)


if __name__ == "__main__":
    main()

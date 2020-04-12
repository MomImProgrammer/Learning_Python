from string import ascii_lowercase

def validate(position):
    if  position[0] in ('Q','R','B') and len(position)==3:
        if is_on_board(to_pos(position[1:3])):
            return ""
        else:
            return "Your piece is not on the board. Try again."
    else:
        return "Position must start with 'Q', 'R', 'B' and be 3-char length. Try again."

def rook_moves(rook_position):
    moves = []
    for i in range(1,9):
        if i != int(rook_position[1]):
            moves.append(rook_position[0]+str(i))
    for j in ascii_lowercase[0:8]:
        if j != rook_position[0]:
            moves.append(j+rook_position[1])
    return moves

def is_on_board(pos):
    return 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7

def to_coord(pos):
    coord = ascii_lowercase[pos[0]]+str(pos[1]+1)
    return coord

def to_pos(coord):
    horiz_index = ascii_lowercase.index(coord[0])
    vert_index = int(coord[1]) - 1
    return (horiz_index, vert_index)

def bishop_moves(bishop_position):

    moves = []
    horiz_index, vert_index = to_pos(bishop_position)

    for i in range(1,8):

        north_east = (horiz_index + i, vert_index + i)
        north_west = (horiz_index + i, vert_index - i)
        south_east = (horiz_index - i, vert_index + i)
        south_west = (horiz_index - i, vert_index - i)

        if is_on_board(north_east):
            moves.append(to_coord(north_east))
        if is_on_board(south_east):
            moves.append(to_coord(south_east))
        if is_on_board(north_west):
            moves.append(to_coord(north_west))
        if is_on_board(south_west):
            moves.append(to_coord(south_west))
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

def cell_to_coord(_cell):
    # example: takes "a1", returns (0, 0)
    return (1, 1)

def coord_to_cell(i, j):
    # takes (0, 0), returns "a1"
    return


def rookMoves(position):
    boardHoriz = ["a", "b", "c", "d", "e", "f", "g", "h"]
    # boardHoriz = "a b c d e f g h".split()

    acceptableMoves = []

    for i in range(8):
        acceptableMoves.append(position[0] + str(i + 1))
        acceptableMoves.append(boardHoriz[i] + position[1])

    acceptableMoves.remove(position)
    acceptableMoves.remove(position)
    acceptableMoves.sort()
    return acceptableMoves

def main():
    print ("Input Rook position on a chess board")
    position = input()
    print (rookMoves (position))

if __name__ == "__main__":
    main()

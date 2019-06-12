def rookMoves (position):
    boardHoriz = ["a","b","c","d","e","f","g","h"]
    acceptableMoves = []
    for i in range(8):
        acceptableMoves.append(position[0] + str(i+1))
        acceptableMoves.append(boardHoriz[i] + position[1])
    acceptableMoves.remove(position)
    acceptableMoves.remove(position)
    acceptableMoves.sort()
    return acceptableMoves

print ("Input Rook position on a chess board")
position = input()
print (rookMoves (position))

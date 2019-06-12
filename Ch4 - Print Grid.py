#Say you have a list of lists where each value in the inner lists is a one-character string, like this:
#grid = [['.', '.', '.', '.', '.', '.'],
#        ['.', 'O', 'O', '.', '.', '.'],
#        ['O', 'O', 'O', 'O', '.', '.'],
#        ['O', 'O', 'O', 'O', 'O', '.'],
#        ['.', 'O', 'O', 'O', 'O', 'O'],
#        ['O', 'O', 'O', 'O', 'O', '.'],
#        ['O', 'O', 'O', 'O', '.', '.'],
#        ['.', 'O', 'O', '.', '.', '.'],
#        ['.', '.', '.', '.', '.', '.']]
#You can think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters.
#The (0, 0) origin will be in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase going down.
#Copy the previous grid value, and write code that uses it to print the image.
#..OO.OO..
#.OOOOOOO.
#.OOOOOOO.
#..OOOOO..
#...OOO...
#....O....

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# for j in range(len(grid[0])):
#     for i in range(len(grid)):
#         if i != len(grid) - 1:
#              print (grid[i][j], end='')
#         else:
#             print (grid[i][j])


# variant #2
def test():
    for row in grid:
        cnt = 0
        for cell in row:
            cnt += 1
            if cnt == len(row):
                print(cell)
            else:
                print(cell, end='')


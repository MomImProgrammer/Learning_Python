'''
Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
Your printTable() function would print the following:

  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
'''

def countColWidth(table):
    colWidths = [0] * len(table)
    for i in range(len(table)):
        for j in range(len(table[i])):
            if colWidths[i] < len(table[i][j]):
                colWidths[i] = len(table[i][j])
    return colWidths

def printTable(table, colWidths):
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colWidths[j]),end=' ')
        print('')
        


if __name__ == "__main__":
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    columnWidth = countColWidth(tableData)
    printTable(tableData, columnWidth)

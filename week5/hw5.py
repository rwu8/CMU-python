#################################################
# Hw5
#################################################

import cs112_s19_week5_linter

#####################################
# COLLABORATIVE Non-Animation Problems
# Collaborators:
#####################################

import copy

def nondestructiveRemoveRowAndCol(lst, row, col):
    copylst = []
    temp = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if i != row and j != col:
                temp.append(lst[i][j])
        if temp == []:
            continue
        else:
            copylst.append(temp)
            temp = []
    return copylst

def destructiveRemoveRowAndCol(lst, row, col):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j == col:
                del lst[i][j]
    del lst[row]
    return None

def bestQuiz(a):
    if a == []: return None
    totalStudents = len(a[0])
    totalQuiz = [0] * totalStudents
    totalGrades = [0] * totalStudents
    bestAverageIndex = -1
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] > 0:
                totalGrades[j] += a[i][j]
                totalQuiz[j] += 1
    averages = [totalGrades[i] / totalQuiz[i] for i in range(len(totalQuiz))]

    for i in range(len(averages)):
        if averages[i] == max(averages):
            return i

#####################################
# Solo Non-Animation Problems
# No collaborators allowed here
#####################################
import math

def areLegalValues(a, n):
    nSquared = n**2
    length = len(a)

    if nSquared != length: return False

    for i in range(length):
        if not isinstance(a[i], int):
            return False
        if a[i] > length:
            return False
        if (a.count(i) > 1 and a[i] != 0):
            return False
    return True

def isLegalRow(board, row):
    temp = board[row]
    n = int(math.sqrt(len(temp)))
    return areLegalValues(temp, n)

def isLegalCol(board, col):
    tempCol = []
    for rowIdx in range(len(board)):
        tempCol.append(board[rowIdx][col])
    n = int(math.sqrt(len(tempCol)))
    return areLegalValues(tempCol, n)

def isLegalBlock(board, block):
    temp = []
    rowMin = 0
    rowMax = 0
    colMin = 0
    colMax = 0
    if block == 0 or block == 1 or block == 2:
        rowMin = 0
        rowMax = 3
    elif block == 3 or block == 4 or block == 5:
        rowMin = 3
        rowMax = 6
    else:
        rowMin = 6
        rowMax = 9
    if block == 0 or block == 3 or block == 6:
        colMin = 0
        colMax = 3
    elif block == 1 or block == 4 or block == 7:
        colMin = 3
        colMax = 6
    else:
        colMin = 6
        colMax = 9

    for rowIdx in range(rowMin,rowMax):
        for colIdx in range(colMin, colMax):
            temp.append(board[rowIdx][colIdx])
    n = int(math.sqrt(len(temp)))
    return areLegalValues(temp, n)

def isLegalSudoku(board):
    for i in range(len(board)):
        if not isLegalRow(board, i) or not isLegalCol(board, i) or not isLegalBlock(board, i):
            return False
    return True

#################################################
# ignore_rest: The autograder will not look at 
# anything below here.  The graphics problems
# will go below.
#################################################

#####################################
# Solo Animation Problem
# No collaborators allowed here
#####################################

from tkinter import *

#### Sudoku Animation ####

def init(data):
    pass

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    pass

def redrawAll(canvas, data):
    pass

def runSudoku(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed    

#################################################
# Test code is below here
#################################################

def testNondestructiveRemoveRowAndCol():
    print("Testing nondestructiveRemoveRowAndCol()... ", end="")
    # The input list and output list
    lst = [[2, 3, 4, 5],
           [8, 7, 6, 5],
           [0, 1, 2, 3]]
    result = [[2, 3, 5],
              [0, 1, 3]]
    # Copy the input list so we can check it later
    import copy
    lstCopy = copy.deepcopy(lst)
    # The first assert is an ordinary test; the second is a non-destructive test
    assert (nondestructiveRemoveRowAndCol(lst, 1, 2) == result)
    assert (lst == lstCopy), "input list should not be changed"
    print('Passed!')

def testDestructiveRemoveRowAndCol():
    # This is a test case for a destructive function.
    print("Testing destructiveRemoveRowAndCol()... ", end="")

    # The input list and output list
    lst = [[2, 3, 4, 5],
           [8, 7, 6, 5],
           [0, 1, 2, 3]]
    result = [[2, 3, 5],
              [0, 1, 3]]
    # The first test is an ordinary test; the second is a destructive test
    assert (destructiveRemoveRowAndCol(lst, 1, 2) == None)
    assert (lst == result), "input list should be changed"
    print('Passed!')


def testBestQuiz():
    print("Testing bestQuiz()... ", end="")
    assert(bestQuiz(a=[[88, 80, 91], [68, 100, -1]]) == 2)
    print('Passed!')

board1 = [
  [ 1, 3, 2, 6, 7, 5, 4, 9, 8 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 7, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 7, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 0, 9 ]
]

board2 = [
  [ 5, 3, 7, 0, 7, 0, 0, 0, 7 ],
  [ 6, 2, 1, 1, 9, 5, 0, 0, 8 ],
  [ 4, 9, 8, 4, 0, 0, 0, 6, 9 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 7, 6, 0, 0, 0, 0, 2, 8, 2 ],
  [ 7, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 0, 4 ]
]

board3 = [
    [5, 1, 7, 6, 9, 8, 2, 3, 4],
    [2, 8, 9, 1, 3, 4, 7, 5, 6],
    [3, 4, 6, 2, 7, 5, 8, 9, 1],
    [6, 7, 2, 8, 4, 9, 3, 1, 5],
    [1, 3, 8, 5, 2, 6, 9, 4, 7],
    [9, 5, 4, 7, 1, 3, 6, 8, 2],
    [4, 9, 5, 3, 6, 2, 1, 7, 8],
    [7, 2, 3, 4, 8, 1, 5, 6, 9],
    [8, 6, 1, 9, 5, 7, 4, 2, 3]]

def testAreLegalValues():
    print("Testing bestQuiz()... ", end="")
    assert (bestQuiz(a=[[88, 80, 91], [68, 100, -1]]) == 2)
    print('Passed!')

def testIsLegalRow():
    print("Testing isLegalRow()... ", end="")
    assert (isLegalRow(board1,0) == True)
    assert (isLegalRow(board2,2) == False)
    print('Passed!')

def testIsLegalCol():
    print("Testing isLegalCol()... ", end="")
    assert (isLegalCol(board1, 1) == False)
    assert (isLegalCol(board2, 8) == True)
    print('Passed!')

def testIsLegalBlock():
    print("Testing isLegalBlock()... ", end="")
    assert (isLegalBlock(board1, 1) == False)
    assert (isLegalBlock(board2, 0) == True)
    print('Passed!')

def testIsLegalSudoku():
    print("Testing isLegalSudoku()... ", end="")
    assert (isLegalSudoku(board1) == False)
    assert (isLegalSudoku(board2) == False)
    assert (isLegalSudoku(board3) == True)
    print('Passed!')

def testSudokuAnimation():
    print("Running Sudoku Animation...", end="")
    # Feel free to change the width and height!
    width = 500
    height = 500
    runSudoku(width, height)
    print("Done!")

def testAll():    
    testNondestructiveRemoveRowAndCol()
    testDestructiveRemoveRowAndCol()
    testBestQuiz()
    testAreLegalValues()
    testIsLegalRow()
    testIsLegalCol()
    testIsLegalBlock()
    testIsLegalSudoku()
    # testSudokuAnimation()

def main():
    cs112_s19_week5_linter.lint() # check rules
    testAll()

if __name__ == '__main__':
    main()
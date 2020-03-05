#################################################
# Hw10
#################################################

import math
import string

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Hw10 problems
#################################################

def getCourse(courseCatalog, courseNumber):
    parentCourse = courseCatalog[0]

    # base case
    if len(courseCatalog) <= 1:
        return None
    # found our course!
    elif courseCatalog[1] == courseNumber:
        return parentCourse + '.' + courseNumber

    # recursive case: next element is a list
    elif isinstance(courseCatalog[1],list):
        subCourse = getCourse(courseCatalog[1], courseNumber)
        if subCourse:
            return parentCourse + '.' + subCourse
    # recursive case: delete subCourse element from search
    return getCourse([parentCourse] + courseCatalog[2:], courseNumber)

def flatten(lst):
    # base case: deepist list
    if not isinstance(lst, list):
        return lst
    # base case: empty list
    if len(lst) == 0:
        return []
    # recursion with non-list element
    if not isinstance(lst[0], list):
        return [lst[0]] + flatten(lst[1:])
    else:
        # recursion with list
        return flatten(lst[0]) + flatten(lst[1:])

def isValid(board, x, y):
    # judge the column
    for i in range(len(board)):
        # if any duplicate numbers in column
        if i != x and board[i][y] == board[x][y]:
            return False

    # judge the row
    for i in range(len(board)):
        # if any duplicate numbers in row
        if i != y and board[x][i] == board[x][y]:
            return False

    # judge the block
    i = x // 3 * 3
    j = y // 3 * 3
    for k in range(len(board)):
        xIdx = i + k // 3
        yIdx = j + k % 3
        if xIdx == x and yIdx == y:
            continue

        if board[xIdx][yIdx] == board[x][y]:
            return False
    return True

def dfs(board, x, y):
    # advance to next row
    if y == 9:
        y = 0
        x += 1

    # complete
    if x >= 9:
        return True

    # skip our solved point
    if board[x][y] != 0:
        return dfs(board, x, y + 1)

    # iterate through all possibilities
    for i in range(9):
        board[x][y] = i+1
        if isValid(board,x,y) and dfs(board,x,y+1):
            return True
        board[x][y] = 0

def solveSudoku(board):
    dfs(board, 0, 0)
    return board

#################################################
# Test code is below here
#################################################

def testGetCourse():
    courseCatalog = ["CMU",
                         ["CIT",
                              ["ECE", "18-100", "18-202", "18-213"],
                              ["BME", "42-101", "42-201"],
                          ],
                         ["SCS",
                              ["CS",
                                   ["Intro", "15-110", "15-112"],
                                   "15-122", "15-150", "15-213"
                               ],
                          ],
                         "99-307", "99-308"
                     ]
    print('Testing getCourse()...', end=" ")
    assert (getCourse(courseCatalog, "18-100") == "CMU.CIT.ECE.18-100")
    assert (getCourse(courseCatalog, "15-112") == "CMU.SCS.CS.Intro.15-112")
    assert (getCourse(courseCatalog, "15-213") == "CMU.SCS.CS.15-213")
    assert (getCourse(courseCatalog, "99-307") == "CMU.99-307")
    assert (getCourse(courseCatalog, "15-251") == None)
    print('Passed!')

def testFlatten():
    print('Testing flatten()...', end=" ")
    assert(flatten([1,[2]]) == [1,2])
    assert(flatten([1,2,[3,[4,5],6],7]) == [1,2,3,4,5,6,7])
    assert(flatten(['wow', [2,[[]]], [True]]) == ['wow', 2, True])
    assert(flatten([]) == [])
    assert(flatten([[]]) == [])
    assert(flatten(3) == 3)
    print('Passed!')

def testSolveSudoku():
    print('Testing solveSudoku()...', end='')
    board = [
              [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
              [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
              [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
              [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
              [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
              [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
              [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
              [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
              [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
            ]
    solved = solveSudoku(board)
    solution = [
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]
               ]
    assert(solved == solution)
    print('Passed!')

def testSolveSudoku2():
    print('Testing solveSudoku()...', end='')
    board = [
              [ 0, 0, 2, 0, 0, 0, 1, 0, 9 ],
              [ 0, 0, 0, 3, 0, 0, 2, 8, 0 ],
              [ 0, 0, 0, 0, 5, 0, 3, 0, 0 ],
              [ 0, 0, 0, 0, 0, 6, 4, 0, 0 ],
              [ 8, 7, 6, 5, 4, 3, 0, 2, 1 ],
              [ 0, 0, 0, 0, 0, 0, 6, 7, 0 ],
              [ 0, 0, 3, 0, 0, 0, 7, 0, 4 ],
              [ 0, 2, 0, 0, 1, 0, 8, 0, 0 ],
              [ 1, 0, 0, 0, 0, 0, 9, 0, 0 ]
            ]
    solved = solveSudoku(board)
    solution = None
    assert(solved == solution)
    print('Passed!')

def testAll():
    testGetCourse()
    testFlatten()
    testSolveSudoku()
    testSolveSudoku2()

def main():
    testAll()

if __name__ == '__main__':
    main()
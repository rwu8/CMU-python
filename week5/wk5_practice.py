#################################################
# Hw4
#################################################

import cs112_s19_week5_linter
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
# Hw5 problems
#################################################

def makeMagicSquare(n):
    if n < 0 or n % 2 == 0:
        return None

    magicSquare = [[0 for x in range(n)]
                      for y in range(n)]

    # initialize position of 1
    row = n / 2
    col = n - 1
    num = 1

    while num <= (n*n):
        #3. row position is -1 & column position is n,
        # the new position would be: (0, n-2).
        if row == -1 and col == n:
            col = n - 2
            row = 0
        else:
            # if next num overflows to the right side
            if col == n:
                col = 0
            # if next num overflows to the upper side
            if row < 0:
                row = n - 1

        # 2. If the magic square already contains a number
        # at the calculated position, calculated column
        # position will be decremented by 2, and
        # calculated row position will be incremented by 1.
        if magicSquare[int(row)][int(col)]:
            col -= 2
            row += 1
            continue
        else:
            magicSquare[int(row)][int(col)] = num
            num += 1

        col += 1
        row -= 1

    # format display of the magicSquare
    for row in range(0,n):
        for col in range(0,n):
            print('%2d ' % (magicSquare[row][col]), end = '')
            # create matrix format
            if col == n - 1:
                print()

    return magicSquare

    #[[1, 2, 3],
    #[2, 3, 1],
    #[3, 1, 2]]
def isLatinSquare(a):
    length = len(a)
    symbols = a[0]

    for row in range(length):
        for item in range(len(a[row])):
            expected = (item + row) % length
            # print(a[row][col])
            if a[row][item] != symbols[expected]:
                return False
    return True

def isKnightsTour(a):
    return 42

#################################################
# Hw5 Test Scripts
#################################################

def testMakeMagicSquare():
    print('testing makeMagicSquare()... ', end="")
    assert(makeMagicSquare(4) == None)
    assert(makeMagicSquare(3) == [[2,7,6], [9,5,1], [4,3,8]])
    print('Passed!')

def testIsLatinSquare():
    print('testing isLatinSquare()... ', end="")
    assert(isLatinSquare([[1, 2, 3], [2, 3, 1], [3, 1, 2]]) == True)
    assert(isLatinSquare([['A', 'B', 'C'], ['B', 'C', 'A'], ['C', 'A', 'B']]) == True)
    assert(isLatinSquare([[4, 2, 3], [2, 3, 1], [3, 1, 2]]) == False)
    print('Passed!')

def testIsKnightsTour():
    print('Testing isKnightsTour()...', end='')
    L = [ [ 38, 41, 18,  3, 22, 27, 16,  1],
          [ 19,  4, 39, 42, 17,  2, 23, 26],
          [ 40, 37, 54, 21, 52, 25, 28, 15],
          [  5, 20, 43, 56, 59, 30, 51, 24],
          [ 36, 55, 58, 53, 44, 63, 14, 29],
          [  9,  6, 45, 62, 57, 60, 31, 50],
          [ 46, 35,  8, 11, 48, 33, 64, 13],
          [  7, 10, 47, 34, 61, 12, 49, 32]
        ]
    assert(isKnightsTour(L) == True)
    L = [ [ 38, 41, 18,  3, 22, 27, 16,  1],
          [ 19,  4, 39, 42, 17,  2, 23, 26],
          [ 40, 37, 54, 21, 52, 25, 28, 15],
          [  5, 20, 43, 56, 59, 30, 51, 24],
          [ 36, 55, 58, 53, 44, 64, 14, 29],
          [  9,  6, 45, 62, 57, 60, 31, 50],
          [ 46, 35,  8, 11, 48, 33, 64, 13],
          [  7, 10, 47, 34, 61, 12, 49, 32]
        ]
    assert(isKnightsTour(L) == False)
    L = [ [ 38, 41, 18,  3, 22, 27, 16,  0],
          [ 19,  4, 39, 42, 17,  2, 23, 26],
          [ 40, 37, 54, 21, 52, 25, 28, 15],
          [  5, 20, 43, 56, 59, 30, 51, 24],
          [ 36, 55, 58, 53, 44, 63, 14, 29],
          [  9,  6, 45, 62, 57, 60, 31, 50],
          [ 46, 35,  8, 11, 48, 33, 64, 13],
          [  7, 10, 47, 34, 61, 12, 49, 32]
        ]
    assert(isKnightsTour(L) == False)
    L = [ [  8, 11, 6,  3],
          [  1,  4, 9, 12],
          [ 10,  7, 2,  5]
        ]
    assert(isKnightsTour(L) == True)
    print('Passed!')

#################################################
# Hw4 Main
#################################################

def testAll():
    testMakeMagicSquare()
    testIsLatinSquare()

def main():
    cs112_s19_week5_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
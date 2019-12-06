#################################################
# Colab1
#################################################

import cs112_s18_week1_linter
import math

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
# Colab1 problems
#################################################

def isPerfectSquare(n):
    if (isinstance(n, int) != True):
        return False
    else:
        if (n == 0): return True
        elif (n > 0):
            tmp = math.sqrt(n)
            if ((tmp % 2 == 1) or (tmp % 2 == 0)):
                return True
    return False

def perfectSquareHandler():
    tmp = input('Enter a number:')
    if isPerfectSquare(int(tmp)):
        print("The number %s is a perfect square" %tmp)
    else:
        print("The number %s is not a perfect square" %tmp)

def nearestOdd(n):
    if (n % 2 == 0):
        return n - 1
    elif (n % 2 == 1):
        return n
    elif (n % 2 < 1):
        return roundHalfUp(n) + 1
    else: return roundHalfUp(n) - 1

def rectanglesOverlap(x1, y1, w1, h1, x2, y2, w2, h2):
    # if ((w1 >= x1 and x2 <= w1)
    #     or (w2 >= x1 and w2 <= x2)) \
    #     or ((h1 >= y1 and h1 <= y2) or (h2 >= y1 and h2 <= y2)):
    #     return True
    if ((w2 + x2) <= (w1 + x1) and (w2 + x2) >= w1
        and ((-y2 <= -y1) and -y2) >= (-y1 - h1)):
        return True
    elif((w2 + x2) <= (w1 + x1) and (x2 + w2) >= x1
         and ((-y2 - h2 <= -y1) and (-x2 - h2) >= (-y1 - h1))):
        return True
    elif (x2 <= (w1 + x1) and x2 >= x1 and ((-y2 - h2 <= -y1)
                                            and (-x2 - h2) >= (-y1 - h1))):
        return True
    elif (x2 <= (w1 + x1) and x2 >= x1 and -y2 <= -y1
          and -x2 >= (-y1 - h1)):
        return True
    elif (-y1 <= -y2 and (-y1 - h1) >= (-y2 - h2) and x1 >= x2
          and (x1 + w1 <= x2 + w2)):
        return True
    return False


def getKthDigit(n, k):
    # integer division returns the requested #'s place
    return abs(n)//(10**k)%10

def setKthDigit(n, k, d=0):
    #first remove the # in the kth place of n, and replace with d
    if (n >= 0):
        return n - getKthDigit(n, k) * 10 ** k + d * 10 ** k
    else:
        tmp = abs(n) - getKthDigit(abs(n), k)*10**k + d*10**k
        return -tmp

#################################################
# Colab1 Test Functions
################################################

def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')
    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(1) == True)
    assert(isPerfectSquare(16) == True)
    assert(isPerfectSquare(1234**2) == True)
    assert(isPerfectSquare(15) == False)
    assert(isPerfectSquare(17) == False)
    assert(isPerfectSquare(-16) == False)
    assert(isPerfectSquare(1234**2+1) == False)
    assert(isPerfectSquare(1234**2-1) == False)
    assert(isPerfectSquare(4.0000001) == False)
    assert(isPerfectSquare('Do not crash here!') == False)
    print('Passed.')

def ioTest(test):
    import sys, io
    myOut = io.StringIO()
    myIn = io.StringIO(test)
    sys.stdout = myOut
    sys.stdin = myIn
    perfectSquareHandler()
    return myOut.getvalue()

def testPerfectSquareHandler():
    import sys
    print('Testing perfectSquareHandler()... ', end='')
    tmpOut = sys.stdout
    tmpIn = sys.stdin
    fourTest = ioTest("4\n")
    sevenTest = ioTest("7\n")
    sys.stdout = tmpOut
    sys.stdin = tmpIn
    # Note: when you test this yourself, you should see:
    # Enter a number:4
    # The number 4 is a perfect square
    # in the interpreter.
    assert(fourTest == "Enter a number:The number 4 is a perfect square\n")
    assert(sevenTest == "Enter a number:The number 7 is not a perfect square\n")
    print('Passed!')

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    print('Passed.')

def testRectanglesOverlap():
    print('Testing rectanglesOverlap()...', end='')
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3,4,5,6) == False)
    print('Passed.')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed.')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    assert(setKthDigit(809, 0) == 800)
    print('Passed.')

#################################################
# Colab1 Main
################################################

def testAll():
    testIsPerfectSquare()
    testPerfectSquareHandler()
    testNearestOdd()
    testGetKthDigit()
    testSetKthDigit()
    testRectanglesOverlap()

def main():
    cs112_s18_week1_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()

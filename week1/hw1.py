#################################################
# Hw1
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
# Hw1 problems
#################################################

# def roc1(x):
#     a = x % 42
#     b = x // 42
#     return a == b and x > 450

def roc1Answer():
    return 473

def getTheCents(n):
    if (isinstance(n, int)): return 0
    elif (isinstance(n, float) == False): return None
    else:
        if ((n * 100 % 1) * 100 / 100 > 0 and
            (n * 100 % 1) * 100 / 100 < 1):
            return int(n * 100 % 100) + 1
        return int(n * 100 % 100)

def playGuessingGame():
    print("Let's play a guessing game! Think of a type of pet.")
    furYN = input("Does it have fur?")
    if (furYN == 'Yes'):
        fetchYN = input('Can you teach it to play fetch?')
        if (fetchYN == 'Yes'):
            print("It's a dog!")
        else:
            print("It's a cat!")
    else:
        swimYN = input('Can it swim?')
        if (swimYN == "Yes"):
            print("It's a fish!")
        else:
            print("It's a bird!")

    return

def distance(x1, y1, x2, y2):
    return math.sqrt((y2 - y1)**2 + (x2 - x1)**2)

def isRightTriangle(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)

    if (almostEqual(c, math.sqrt(a**2 + b**2))): return True
    elif (almostEqual(a, math.sqrt(b**2 + c**2))): return True
    elif (almostEqual(b, math.sqrt(a**2 + c**2))): return True
    return False

def bonusFindIntRootsOfCubic(a, b, c, d):
    return

#################################################
# Hw1 Test Functions
#################################################

def roc1(x):
    a = x % 42
    b = x // 42
    return a == b and x > 450

def testRoc1Answer():
    print("Testing roc1Answer()...", end="")
    answer = roc1Answer()
    assert(roc1(answer) == True)
    print("Passed.")

def testGetTheCents():
    print("Testing getTheCents()...", end="")
    assert(getTheCents(10.95) == 95)
    assert(getTheCents(0.25) == 25)
    assert(getTheCents(10.5) == 50)
    assert(getTheCents(4.0) == 0)
    assert(getTheCents(2) == 0)
    assert(getTheCents(3.299) == 30)
    assert(getTheCents(2.961) == 97)
    assert(getTheCents("money") == None)
    assert(getTheCents(None) == None)
    print("Passed.")

def ioTest(test):
    import sys, io
    myOut = io.StringIO()
    myIn = io.StringIO(test)
    sys.stdout = myOut
    sys.stdin = myIn
    playGuessingGame()
    return myOut.getvalue()

def testPlayGuessingGame():
    import sys
    print("Testing playGuessingGame()...", end="")
    tmpOut = sys.stdout
    tmpIn = sys.stdin
    dogTest = ioTest("Yes\nYes\n")
    catTest = ioTest("Yes\nNo\n")
    fishTest = ioTest("No\nYes\n")
    birdTest = ioTest("No\nNo\n")
    sys.stdout = tmpOut
    sys.stdin = tmpIn
    assert(dogTest == "Let's play a guessing game! Think of a type of pet.\n"+\
            "Does it have fur?Can you teach it to play fetch?It's a dog!\n")
    assert(catTest == "Let's play a guessing game! Think of a type of pet.\n"+\
            "Does it have fur?Can you teach it to play fetch?It's a cat!\n")
    assert(fishTest == "Let's play a guessing game! Think of a type of pet.\n"+\
            "Does it have fur?Can it swim?It's a fish!\n")
    assert(birdTest == "Let's play a guessing game! Think of a type of pet.\n"+\
            "Does it have fur?Can it swim?It's a bird!\n")
    print("Passed.")

def testDistance():
    print("Testing distance()...", end="")
    assert(almostEqual(distance(0, 0, 1, 1), 2**0.5))
    assert(almostEqual(distance(3, 3, -3, -3), 6*2**0.5))
    assert(almostEqual(distance(20, 20, 23, 24), 5))
    print("Passed. (Add more tests to be more sure!)")

def testIsRightTriangle():
    print('Testing isRightTriangle()... ', end='')
    assert(isRightTriangle(0, 0, 0, 3, 4, 0) == True)
    assert(isRightTriangle(1, 1.3, 1.4, 1, 1, 1) == True)
    assert(isRightTriangle(9, 9.12, 8.95, 9, 9, 9) == True)
    assert(isRightTriangle(0, 0, 0, math.pi, math.e, 0) == True)
    assert(isRightTriangle(0, 0, 1, 1, 2, 0) == True)
    assert(isRightTriangle(0, 0, 1, 2, 2, 0) == False)
    assert(isRightTriangle(1, 0, 0, 3, 4, 0) == False)
    print('Passed.')


def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

def testBonusFindIntRootsOfCubic():
    print('Testing findIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed.')

#################################################
# Hw1 Main
#################################################

def testAll():
    testRoc1Answer()
    testGetTheCents()
    testPlayGuessingGame()
    testDistance()
    testIsRightTriangle()
    testBonusFindIntRootsOfCubic()

def main():
    cs112_s18_week1_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()

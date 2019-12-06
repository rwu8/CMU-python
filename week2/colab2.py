#################################################
# Colab2
#################################################

import cs112_s18_week2_linter
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
# Colab2 problems
#################################################

def rotateNumber(x):
    return 42

def isCircularPrime(x):
    return 42

def nthCircularPrime(n):
    return 42

def countLowercaseUpToPercent(s):
    return 42

def longestCommonSubstring(s1, s2):
    return 42

def gradebookSummary(gradebookFilename):
    return 42

#################################################
# Colab2 Test Functions
################################################

def testRotateNumber():
    print('Testing rotateNumber()... ', end='')
    assert(rotateNumber(1234) == 4123)
    assert(rotateNumber(4123) == 3412)
    assert(rotateNumber(3412) == 2341)
    assert(rotateNumber(2341) == 1234)
    assert(rotateNumber(5) == 5)
    assert(rotateNumber(111) == 111)
    print('Passed!')

def testIsCircularPrime():
    print('Testing isCircularPrime()... ', end='')
    assert(isCircularPrime(2) == True)
    assert(isCircularPrime(11) == True)
    assert(isCircularPrime(13) == True)
    assert(isCircularPrime(79) == True)
    assert(isCircularPrime(197) == True)
    assert(isCircularPrime(1193) == True)
    print('Passed!')

def testNthCircularPrime():
    print('Testing nthCircularPrime()... ', end='')
    assert(nthCircularPrime(0) == 2)
    assert(nthCircularPrime(4) == 11)
    assert(nthCircularPrime(5) == 13)
    assert(nthCircularPrime(11) == 79)
    assert(nthCircularPrime(15) == 197)
    assert(nthCircularPrime(25) == 1193)
    print('Passed!')

def testCountLowercaseUpToPercent():
    print('Testing countLowercaseUpToPercent()...', end='')
    assert(countLowercaseUpToPercent("abCDe") == 3)
    assert(countLowercaseUpToPercent("WxyZ") == 2)
    assert(countLowercaseUpToPercent("Journey Before %Destination") == 11)
    assert(countLowercaseUpToPercent("%Testing, testing, 123%") == 0)
    assert(countLowercaseUpToPercent("Here`s some {weird} chars") == 18)
    assert(countLowercaseUpToPercent("") == 0)
    print('Passed!')

def testLongestCommonSubstring():
    print("Testing longestCommonSubstring()...", end="")
    assert(longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert(longestCommonSubstring("abcdef", "ghi") == "")
    assert(longestCommonSubstring("", "abqrcdest") == "")
    assert(longestCommonSubstring("abcdef", "") == "")
    assert(longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    print("Passed!")

def testGradebookSummary():
    print("Testing gradebookSummary()...", end="")
    assert(gradebookSummary("sampleFiles/gradebook1.txt") == 
            "wilma\t92.67\nfred\t90.40\nbetty\t88.00")
    assert(gradebookSummary("sampleFiles/gradebook2.txt") == 
            "wilma\t92.67\nfred\t90.40\nbetty\t88.00")
    assert(gradebookSummary("sampleFiles/small1.txt") == 
            "fred\t0.00")
    assert(gradebookSummary("sampleFiles/small2.txt") == 
            "fred\t-1.00\nwilma\t-2.00")
    assert(gradebookSummary("sampleFiles/small3.txt") == 
            "fred\t100.50")
    assert(gradebookSummary("sampleFiles/small4.txt") == 
            "fred\t49.00\nwilma\t50.00")
    print("Passed!")

#################################################
# Colab2 Main
################################################

def testAll():
    testRotateNumber()
    testIsCircularPrime()
    testNthCircularPrime()
    testCountLowercaseUpToPercent()
    testLongestCommonSubstring()
    testGradebookSummary()

def main():
    cs112_s18_week2_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()

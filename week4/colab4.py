#################################################
# Colab4
#################################################

import cs112_s18_week4_linter
import math
import string
import copy

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
# Colab4 problems
########################

def lookAndSay(a):
    return 42

def solvesCryptarithm(puzzle, solution):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *

def drawStar(canvas, centerX, centerY, diameter, numPoints, color):
    canvas.create_text(centerX, centerY, text="return 42", font="Arial 20 bold")

def drawStarHelper(centerX, centerY, diameter, numPoints, color, 
                   winWidth=500, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()

    drawStar(canvas, centerX, centerY, diameter, numPoints, color)

    root.mainloop()

def drawUnitedStatesFlag(winWidth=950, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()

    canvas.create_text(winWidth/2, winHeight/2,
                       text="return 42", font="Arial 20 bold")

    root.mainloop()

def testDrawStar():
    print("Testing drawStar()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    drawStarHelper(250, 250, 500, 5, "gold")
    drawStarHelper(300, 400, 100, 4, "blue")
    drawStarHelper(300, 200, 300, 9, "red")
    print("Done!")

def testDrawUnitedStatesFlag():
    print("Testing drawUnitedStatesFlag()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    drawUnitedStatesFlag()
    drawUnitedStatesFlag(winWidth=570, winHeight=300)
    print("Done!")

#################################################
# Colab4 Test Functions
#########################################################################

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def testSolvesCryptarithm():
    print("Testing solvesCryptarithm()...", end="")
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDRS"))
    # from http://www.cryptarithms.com/default.asp?pg=1
    assert(solvesCryptarithm("NUMBER+NUMBER=PUZZLE", "UMNZP-BLER"))
    assert(solvesCryptarithm("TILES+PUZZLES=PICTURE", "UISPELCZRT"))
    assert(solvesCryptarithm("COCA+COLA=OASIS", "LOS---A-CI"))
    assert(solvesCryptarithm("CROSS+ROADS=DANGER", "-DOSEARGNC"))

    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDR-") == False)
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY-ENDRS") == False)
    assert(solvesCryptarithm("SEND+MORE=MONY","OMY--ENDRS") == False)
    assert(solvesCryptarithm("SEND+MORE=MONEY","MOY--ENDRS") == False)
    print("Passed!")

#################################################
# Colab4 Main
################################################

def testAll():
    testLookAndSay()
    testSolvesCryptarithm()
    testDrawStar()
    testDrawUnitedStatesFlag()

def main():
    cs112_s18_week4_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()

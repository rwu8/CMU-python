#################################################
# Hw4
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
# Hw4 problems
#################################################

"""
Fill in your answers to the List Function Table problem here.

a = a + b            Non-Destructively (Creating New Lists) 
a += b               Destructively (Modifying Lists) 
a.append(x)          Destructively (Modifying Lists)   
a.insert(0, x)       Destructively (Modifying Lists) 
a.extend(b)          Destructively (Modifying Lists) 
a.remove(x)          Destructively (Modifying Lists) 
a.pop(0)             Destructively (Modifying Lists) 
del a[0]             Destructively (Modifying Lists) 
a.reverse()          Destructively (Modifying Lists) 
reversed(a)
a.sort()             Destructively (Modifying Lists) 
sorted(a)            Non-Destructively
copy.copy(a)         Non-Destructively
"""

from collections import Counter

def lookAndSay(a):
    if a == []: return []
    solution = []
    prev = None
    counter = 1

    for i in range(len(a)):
        if i == 0:
            prev = a[i]
            continue
        elif a[i] == prev:
            counter += 1
        else:
            solution.append((counter, prev))
            counter += 1
        prev = a[i]
    solution.append((counter, prev))
    return solution

def inverseLookAndSay(a):
    solution = []

    for i in range(len(a)):
        for j in range(a[i][0]):
            solution.append(a[i][1])
    return solution

def isSubset(a,b):
    for letter in string.ascii_lowercase:
        if a.count(letter) > b.count(letter):
            return False
    return True

def calculateScore(scores, word):
    score = 0
    for letter in word:
        score += scores[ord(letter) - ord('a')]
    return score

def bestScrabbleScore(dictionary, letterScores, hand):
    result = ('', 0)
    word_arr, bestScore = result
    for word in dictionary:
        if isSubset(word, hand):
            score = calculateScore(letterScores, word)
            if bestScore < score:
                word_arr = word
                bestScore = score
            elif bestScore == score:
                if isinstance(word_arr, str):
                    word_arr = [word_arr, word]
                else:
                    word_arr = word_arr + [word]
    result = (word_arr, bestScore)
    if word_arr == [] or word_arr == '':
        return None

    return result


######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *

def drawChessboard(winWidth=640, winHeight=640):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()

    canvas.create_text(winWidth/2, winHeight/2,
                       text="return 42", font="Arial 20 bold")

    root.mainloop()

##### Bonus #####


#################################################
# Hw4 Test Functions
#################################################

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")

def testDrawChessboard():
    print("Testing drawChessboard()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    drawChessboard()
    drawChessboard(winWidth=400, winHeight=400)
    print("Done!")



#################################################
# Hw4 Main
#################################################

def testAll():
    testInverseLookAndSay()
    testBestScrabbleScore()
    # testDrawChessboard()

def main():
    cs112_s18_week4_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()

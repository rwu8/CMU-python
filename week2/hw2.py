#################################################
# Hw2
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
# Hw2 problems
#################################################

def roc2Answer():
    return

def sumOfSquaresOfDigits(x):
    return 42

def isHappyNumber(x):
    return 42

def nthHappyPrime(n):
    return 42
    
def patternedMessage(msg, pattern):
    return 42

def quoteWordCount(script):
    return 42

##### Bonus #####

def play112(game):
    return 42

#################################################
# Hw2 Test Functions
#################################################

def roc2(s):
    a = 0
    b = 0
    for i in range(1, len(s), 2):
        if s[i] in s[:i]:
            continue
        elif s[i] in string.whitespace:
            a += 1
        elif "A" <= s[i] <= "Z":
            b += 1
    return len(s) < 10 and a > 1 and a == b

def testRoc2Answer():
    print("Testing roc2Answer()...", end="")
    answer = roc2Answer()
    assert(roc2(answer) == True)
    print("Passed.")

def testSumOfSquaresOfDigits():
    print('Testing sumOfSquaresOfDigits()... ', end='')
    assert(sumOfSquaresOfDigits(5) == 25)
    assert(sumOfSquaresOfDigits(12) == 5)
    assert(sumOfSquaresOfDigits(234) == 29)
    print('Passed!')

def testIsHappyNumber():
    print('Testing isHappyNumber()... ', end='')
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print('Passed!')

def testNthHappyPrime():
    print('Testing nthHappyPrime()... ', end='')
    assert(nthHappyPrime(0) == 7)
    assert(nthHappyPrime(1) == 13)
    assert(nthHappyPrime(2) == 19)
    assert(nthHappyPrime(3) == 23)
    assert(nthHappyPrime(4) == 31)
    assert(nthHappyPrime(5) == 79)
    assert(nthHappyPrime(6) == 97)
    print('Passed!')
    
def testPatternedMessage():
    print("Testing patternedMessage()...", end="")
    pattern1 = """
***************
******   ******
***************
"""
    result1 = """
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
    assert(patternedMessage("Go Pirates!!!", pattern1).strip("\n") == 
            result1.strip("\n"))

    pattern2 = """
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""
    result2 = """
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""
    assert(patternedMessage("Three Diamonds!",pattern2).strip("\n") == 
            result2.strip("\n"))

    pattern3 = """
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
"""
    result3 = """
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
    assert(patternedMessage("Go Steelers!",pattern3).strip("\n") == 
            result3.strip("\n"))

    pattern4 = """
*** *** ***
** ** ** **
"""
    result4 = """
A-C D?A -CD
?A -C D? A-
"""
    assert(patternedMessage("A-C D?", pattern4).strip("\n") == 
            result4.strip("\n"))
    
    assert(patternedMessage("A", "x y z").strip("\n") == "A A A".strip("\n"))
    assert(patternedMessage("The pattern is empty!", "").strip("\n") == "")
    print("Passed!")

def testQuoteWordCount():
    print("Testing simpleScreenplayWordCount()...", end="")
    quote1 = "Buttercup: You mock my pain.\n" + \
             "Man in Black: Life is pain, Highness. " + \
             "Anyone who says differently is selling something."
    assert(quoteWordCount(quote1) == 15)
    quote2 = "Inigo Montoya: Hello. My name is Inigo Montoya. " + \
             "You killed my father. Prepare to die."
    assert(quoteWordCount(quote2) == 13)
    quote3 = "Costello: You know the fellows' names?\n" + \
             "Abbott: Yes.\n" + \
             "Costello: Well, then who's playing first?\n" + \
             "Abbott: Yes.\n" + \
             "Costello: I mean the fellow's name on first base.\n" + \
             "Abbott: Who."
    assert(quoteWordCount(quote3) == 21)
    quote4 = "Martin Luther King Jr.: " + \
             "The first question which the priest and the Levite asked was:" + \
             " 'If I stop to help this man, what will happen to me?' " + \
             "But... the good Samaritan reversed the question: " + \
             "'If I do not stop to help this man, what will happen to him?'"
    assert(quoteWordCount(quote4) == 44)
    quote5 = "Unknown: Only half of programming is coding. " + \
             "The other 90 percent is debugging."
    assert(quoteWordCount(quote5) == 11) # yes, 11; 90 doesn't count as a word
    quote6 = "Judge Clarence Thomas: "
    assert(quoteWordCount(quote6) == 0)
    quote7 = "Tommy Tutone: 867 - 5309"
    assert(quoteWordCount(quote7) == 0)
    assert(quoteWordCount("") == 0)
    print("Passed!")

def testBonusPlay112():
    print("Testing play112()... ", end="")
    assert(play112( 5 ) == "88888: Unfinished!")
    assert(play112( 521 ) == "81888: Unfinished!")
    assert(play112( 52112 ) == "21888: Unfinished!")
    assert(play112( 5211231 ) == "21188: Unfinished!")
    assert(play112( 521123142 ) == "21128: Player 2 wins!")
    assert(play112( 521123151 ) == "21181: Unfinished!")
    assert(play112( 52112315142 ) == "21121: Player 1 wins!")
    assert(play112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(play112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(play112( 51211 ) == "28888: Player 2: occupied!")
    assert(play112( 5122221 ) == "22888: Player 1: occupied!")
    assert(play112( 51261 ) == "28888: Player 2: offboard!")
    assert(play112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

#################################################
# Hw2 Main
#################################################

def testAll():
    testRoc2Answer()
    testSumOfSquaresOfDigits()
    testIsHappyNumber()
    testNthHappyPrime()
    testPatternedMessage()
    testQuoteWordCount()
    testBonusPlay112()

def main():
    cs112_s18_week2_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()

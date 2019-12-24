# mastermind.py
# for Recitation 3 (15-110 Spring 2011)

################################################
# colorAndPositionMatches
################################################

def colorAndPositionMatches(target, guess):
    # return the number of exact matches (color and position)
    # assumes target and guess are same length
    return 42 # You write this!

def testColorAndPositionMatches():
    print "Testing colorAndPositionMatches()...",
    assert(colorAndPositionMatches("abcde", "bbbbb") == 1)
    assert(colorAndPositionMatches("abcde", "bcdea") == 0)
    assert(colorAndPositionMatches("abcde", "bbbdd") == 2)
    assert(colorAndPositionMatches("abcde", "bbbdd") == 2)
    assert(colorAndPositionMatches("abccc", "cccbb") == 1)
    assert(colorAndPositionMatches("abccc", "acccb") == 3)
    assert(colorAndPositionMatches("qzrmwq", "zzmrqq") == 2)
    print "Passed!"

################################################
# onlyColorMatches
################################################

def onlyColorMatches(target, guess):
    # return the number of partial matches (color but not position)
    # assumes target and guess are same length
    # also assumes target is composed of lowercase letters
    # First find the total matches (same color, any position)
    return 42 # You write this!

def testOnlyColorMatches():
    print "Testing onlyColorMatches()...",
    assert(onlyColorMatches("abcde", "bbbbb") == 0)
    assert(onlyColorMatches("abcde", "bcdea") == 5)
    assert(onlyColorMatches("abcde", "bbbdd") == 0)
    assert(onlyColorMatches("abcde", "bbbdd") == 0)
    assert(onlyColorMatches("abccc", "cccbb") == 3)
    assert(onlyColorMatches("abccc", "acccb") == 2)
    assert(onlyColorMatches("qzrmwq", "zzmrqq") == 3)
    print "Passed!"

################################################
# getRandomTarget
################################################

# Students are provided the code in this section, and are not
# responsible for understanding getRandomTarget, just using it.

def getRandomTarget(targetSize):
    import time 
    # We can't use Python's random functions until CLEESE 0.11, so
    # we'll use our own pseudorandom numbers
    prime1 = 583621
    prime2 = 329717
    prime3 = 611953
    seed = int(100*time.time()) % prime3
    target = ""
    for i in range(targetSize):
        seed = (((seed * prime1) + (seed * seed * prime2)) % prime3)
        target += chr(ord('a') + (seed % targetSize))
    return target

################################################
# playMastermind
################################################

def playMastermind():
    return 42 # You write this!

def testAll():
    testColorAndPositionMatches()
    testOnlyColorMatches()

testAll()
playMastermind()

#################################################
# Week2 Practice
#################################################

import cs112_s18_week2_linter
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
# Tue Lecture
#################################################

def digitCount(n):
    return 42

def hasConsecutiveDigits(n):
    return 42

def gcd(x, y):
    return 42

def pi(n):
    return 42

def h(n):
    return 42

def estimatedPi(n):
    return 42

def estimatedPiError(n):
    return 42

def sumOfDigits(n):
    return 42

def nthAdditivePrime(n):
    return 42

def nthPerfectNumber(n):
    return 42

def vowelCount(s):
    return 42

def interleave(s1, s2):
    return 42

def hasBalancedParentheses(s):
    return 42

#################################################
# Wed Recitation
#################################################

def longestDigitRun(n):
    return 42

def longestIncreasingRun(n):
    return 42

def nthPalindromicPrime(n):
    return 42

def nthLeftTruncatablePrime(n):
    return 42

def nthCarolPrime(n):
    return 42

def rotateStringLeft(s, k):
    return 42

def rotateStringRight(s, k):
    return 42

def wordWrap(text, width):
    return 42

def largestNumber(s):
    return 42

#################################################
# Thu Lecture
#################################################

def sumOfSquaresOfDigits(n):
    return 42

def isHappyNumber(n):
    return 42

def nthHappyNumber(n):
    return 42

def isHappyPrime(n):
    return 42

def nthHappyPrime(n):
    return 42

def mostFrequentDigit(n):
    return 42

def nthPowerfulNumber(n):
    return 42

def nthCircularPrime(n):
    return 42

def findZeroWithBisection(f, x0, x1, epsilon):
    return 42

def longestSubpalindrome(s):
    return 42

def leastFrequentLetters(s):
    return 42

#################################################
# Extra Practice
#################################################

def sameChars(s1, s2):
    return 42

def mostFrequentLetters(s):
    return 42

def areAnagrams(s1, s2):
    return 42

def collapseWhitespace(s):
    return 42

def replace(s1, s2, s3):
    return 42

def encodeOffset(s, d):
    return 42

def decodeOffset(s, d):
    return 42

def encrypt(msg, pwd):
    return 42

def decrypt(msg, pwd):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testDigitCount():
    print('Test digitCount()...', end='')
    assert(digitCount(0) == 1)
    assert(digitCount(5) == 1)
    assert(digitCount(-5) == 1)
    assert(digitCount(42) == 2)
    assert(digitCount(-42) == 2)
    assert(digitCount(121) == 3)
    assert(digitCount(-121) == 3)
    assert(digitCount(-10002000) == 8)
    print('Passed')

def testHasConsecutiveDigits():
    print('Testing hasConsecutiveDigits()... ', end='')
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(123456789) == False)
    assert(hasConsecutiveDigits(1212) == False)
    assert(hasConsecutiveDigits(1212111212) == True)
    assert(hasConsecutiveDigits(33) == True)
    assert(hasConsecutiveDigits(330) == True)
    assert(hasConsecutiveDigits(3003) == True)
    assert(hasConsecutiveDigits(-1212111212) == True)
    print('Passed.')

def testGcd():
    print('Testing gcd()... ', end='')
    assert(gcd(3, 3) == 3)
    assert(gcd(3**6, 3**6) == 3**6)
    assert(gcd(3**6, 2**6) == 1)
    assert (gcd(2*3*4*5,3*5) == 15)
    x = 1568160 # 2**5 * 3**4 * 5**1 *        11**2
    y = 3143448 # 2**3 * 3**6 *        7**2 * 11**1
    g =    7128 # 2**3 * 3**4 *               11**1
    assert(gcd(x, y) == g)
    print('Passed.')

def testPi():
    print('Testing pi()... ', end='')
    assert(pi(1) == 0)
    assert(pi(2) == 1)
    assert(pi(3) == 2)
    assert(pi(4) == 2)
    assert(pi(5) == 3)
    assert(pi(100) == 25)  # there are 25 primes in the range [2,100]
    print('Passed.')

def testH():
    print('Testing h()... ', end='')
    assert(almostEqual(h(0),0))
    assert(almostEqual(h(1),1/1            ))  # h(1) = 1/1
    assert(almostEqual(h(2),1/1 + 1/2      ))  # h(2) = 1/1 + 1/2
    assert(almostEqual(h(3),1/1 + 1/2 + 1/3))  # h(3) = 1/1 + 1/2 + 1/3
    print('Passed.')

def testEstimatedPi():
    print('Testing estimatedPi()... ', end='')
    assert(estimatedPi(100) == 27)
    print('Passed.')

def testEstimatedPiError():
    print('Testing estimatedPi()... ', end='')
    assert(estimatedPiError(100) == 2) # pi(100) = 25, estimatedPi(100) = 27
    assert(estimatedPiError(200) == 0) # pi(200) = 46, estimatedPi(200) = 46
    assert(estimatedPiError(300) == 1) # pi(300) = 62, estimatedPi(300) = 63
    assert(estimatedPiError(400) == 1) # pi(400) = 78, estimatedPi(400) = 79
    assert(estimatedPiError(500) == 1) # pi(500) = 95, estimatedPi(500) = 94
    print('Passed.')

def testNthPrime():
    print('Testing nthPrime()... ', end='')
    assert(nthPrime(0) == 2)
    assert(nthPrime(1) == 3)
    assert(nthPrime(2) == 5)
    assert(nthPrime(3) == 7)
    assert(nthPrime(10) == 31)
    assert(nthPrime(20) == 73)
    assert(nthPrime(30) == 127)
    print('Passed.')

def testNthAdditivePrime():
    print('Testing nthAdditivePrime()... ', end='')
    assert(nthAdditivePrime(0) == 2)
    assert(nthAdditivePrime(1) == 3)
    assert(nthAdditivePrime(5) == 23)
    assert(nthAdditivePrime(10) == 61)
    assert(nthAdditivePrime(15) == 113)
    print('Passed.')

def testNthPerfectNumber():
    print('Testing nthPerfectNumber()... ', end='')
    assert(nthPerfectNumber(0) == 6)
    assert(nthPerfectNumber(1) == 28)
    assert(nthPerfectNumber(2) == 496)  
    assert(nthPerfectNumber(3) == 8128) # this can be slow 
    print('Passed.')

def testLongestDigitRun():
    print('Testing longestDigitRun()... ', end='')
    assert(longestDigitRun(117773732) == 7)
    assert(longestDigitRun(-677886) == 7)
    assert(longestDigitRun(5544) == 4)
    assert(longestDigitRun(1) == 1)
    assert(longestDigitRun(0) == 0)
    assert(longestDigitRun(22222) == 2)
    assert(longestDigitRun(111222111) == 1)
    print('Passed.')

def testLongestIncreasingRun():
    print('Testing longestIncreasingRun()... ', end='')
    assert(longestIncreasingRun(27648923679) == 23679)
    assert(longestIncreasingRun(123345) == 345)
    assert(longestIncreasingRun(1232) == 123)
    assert(longestIncreasingRun(0) == 0)
    assert(longestIncreasingRun(1) == 1)
    assert(longestIncreasingRun(10012301230123) == 123)
    assert(longestIncreasingRun(12345678987654321) == 123456789)
    print('Passed.')

def testNthPalindromicPrime():
    print('Testing nthPalindromicPrime()... ', end='')
    assert(nthPalindromicPrime(0) == 2)
    assert(nthPalindromicPrime(1) == 3)
    assert(nthPalindromicPrime(5) == 101)
    assert(nthPalindromicPrime(10) == 313)
    print('Passed.')

def testNthLeftTruncatablePrime():
    print('Testing nthLeftTruncatablePrime()... ', end='')
    assert(nthLeftTruncatablePrime(0) == 2)
    assert(nthLeftTruncatablePrime(10) == 53)
    assert(nthLeftTruncatablePrime(1) == 3)
    assert(nthLeftTruncatablePrime(5) == 17)
    print('Passed.')

def testNthCarolPrime():
    print('Testing nthCarolPrime()... ', end='')
    assert(nthCarolPrime(0) == 7)
    assert(nthCarolPrime(1) == 47)
    assert(nthCarolPrime(3) == 3967)
    assert(nthCarolPrime(6) == 16769023)
    print('Passed.')

def testSumOfSquaresOfDigits():
    print("Testing sumOfSquaresOfDigits()...", end="")
    assert(sumOfSquaresOfDigits(5) == 25)   # 5**2 = 25
    assert(sumOfSquaresOfDigits(12) == 5)   # 1**2 + 2**2 = 1+4 = 5
    assert(sumOfSquaresOfDigits(234) == 29) # 2**2 + 3**2 + 4**2 = 4+9+16 = 29
    print("Passed.")

def testIsHappyNumber():
    print("Testing isHappyNumber()...", end="")
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print("Passed.")

def testNthHappyNumber():
    print("Testing nthHappyNumber()...", end="")
    assert(nthHappyNumber(0) == 1)
    assert(nthHappyNumber(1) == 7)
    assert(nthHappyNumber(2) == 10)
    assert(nthHappyNumber(3) == 13)
    assert(nthHappyNumber(4) == 19)
    assert(nthHappyNumber(5) == 23)
    assert(nthHappyNumber(6) == 28)
    assert(nthHappyNumber(7) == 31)
    print("Passed.")

def testIsHappyPrime():
    print("Testing isHappyPrime()...", end="")
    assert(isHappyPrime(1) == False)
    assert(isHappyPrime(2) == False)
    assert(isHappyPrime(3) == False)
    assert(isHappyPrime(7) == True)
    assert(isHappyPrime(10) == False)
    assert(isHappyNumber(13) == True)
    print("Passed.")

def testNthHappyPrime():
    print("Testing nthHappyPrime...", end="")
    assert(nthHappyPrime(0) == 7)
    assert(nthHappyPrime(1) == 13)
    assert(nthHappyPrime(2) == 19)
    assert(nthHappyPrime(3) == 23)
    assert(nthHappyPrime(4) == 31)
    assert(nthHappyPrime(10) == 167)
    assert(nthHappyPrime(20) == 397)
    print("Passed.")

def testMostFrequentDigit():
    print('Testing mostFrequentDigit()... ', end='')
    assert(mostFrequentDigit(0) == 0)
    assert(mostFrequentDigit(1223) == 2)
    assert(mostFrequentDigit(12233) == 2)
    assert(mostFrequentDigit(-112233) == 1)
    assert(mostFrequentDigit(1223322332) == 2)
    assert(mostFrequentDigit(123456789) == 1)
    assert(mostFrequentDigit(1234567789) == 7)
    assert(mostFrequentDigit(1000123456789) == 0)
    print('Passed.')

def testNthPowerfulNumber():
    print('Testing nthPowerfulNumber()... ', end='')
    assert(nthPowerfulNumber(0) == 1)
    assert(nthPowerfulNumber(1) == 4)
    assert(nthPowerfulNumber(2) == 8)
    assert(nthPowerfulNumber(3) == 9)
    assert(nthPowerfulNumber(4) == 16)
    assert(nthPowerfulNumber(5) == 25)
    assert(nthPowerfulNumber(10) == 64)
    assert(nthPowerfulNumber(15) == 121)
    assert(nthPowerfulNumber(20) == 196)
    print('Passed.')

def testNthCircularPrime():
    print('Testing nthCircularPrime()... ', end='')
    assert(nthCircularPrime(0) == 2)
    assert(nthCircularPrime(1) == 3)
    assert(nthCircularPrime(2) == 5)
    assert(nthCircularPrime(10) == 73)
    assert(nthCircularPrime(15) == 197)
    assert(nthCircularPrime(16) == 199)
    print('Passed.')

def testFindZeroWithBisection():
    print('Testing findZeroWithBisection()... ', end='')
    def f1(x): return x*x - 2 # root at x=sqrt(2)
    x = findZeroWithBisection(f1, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.41421356192))   
    def f2(x): return x**2 - (x + 1)  # root at x=phi
    x = findZeroWithBisection(f2, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.61803398887))
    def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0
    x = findZeroWithBisection(f3, 1, 2, 0.000000001)
    assert(almostEqual(x, 1.17727855081))
    print('Passed.')


def testVowelCount():
    print("Testing vowelCount()...", end="")
    assert(vowelCount("abcdefg") == 2)
    assert(vowelCount("ABCDEFG") == 2)
    assert(vowelCount("") == 0)
    assert(vowelCount("This is a test.  12345.") == 4)
    assert(vowelCount(string.ascii_lowercase) == 5)
    assert(vowelCount(string.ascii_lowercase*100) == 500)
    assert(vowelCount(string.ascii_uppercase) == 5)
    assert(vowelCount(string.punctuation) == 0)
    assert(vowelCount(string.whitespace) == 0)
    print("Passed!")

def testInterleave():
    print("Testing interleave()...", end="")
    assert(interleave("abcdefg", "abcdefg") == "aabbccddeeffgg")
    assert(interleave("abcde", "abcdefgh") == "aabbccddeefgh")
    assert(interleave("abcdefgh","abcde") == "aabbccddeefgh")
    assert(interleave("Smlksgeneg n a!", "a ie re gsadhm") ==
                      "Sam likes green eggs and ham!")
    assert(interleave("","") == "")
    print("Passed!")

def testHasBalancedParentheses():
    print("Testing hasBalancedParentheses()...", end="")
    assert(hasBalancedParentheses("()") == True)
    assert(hasBalancedParentheses("") == True)
    assert(hasBalancedParentheses("())") == False)
    assert(hasBalancedParentheses("()(") == False) 
    assert(hasBalancedParentheses(")(") == False)
    assert(hasBalancedParentheses("(()())") == True)
    assert(hasBalancedParentheses("((()())(()(()())))") == True)
    assert(hasBalancedParentheses("((()())(()((()())))") == False)
    assert(hasBalancedParentheses("((()())(((()())))") == False)
    print("Passed!")

def testRotateStringLeft():
    print("Testing rotateStringLeft()...", end="")
    assert(rotateStringLeft("abcde", 0) == "abcde")
    assert(rotateStringLeft("abcde", 1) == "bcdea")
    assert(rotateStringLeft("abcde", 2) == "cdeab")
    assert(rotateStringLeft("abcde", 3) == "deabc")
    assert(rotateStringLeft("abcde", 4) == "eabcd")
    assert(rotateStringLeft("abcde", 5) == "abcde")
    assert(rotateStringLeft("abcde", 25) == "abcde")
    assert(rotateStringLeft("abcde", 28) == "deabc")
    print("Passed!")

def testRotateStringRight():
    print("Testing rotateStringRight()...", end="")
    assert(rotateStringRight("abcde", 0) == "abcde")
    assert(rotateStringRight("abcde", 1) == "eabcd")
    assert(rotateStringRight("abcde", 2) == "deabc")
    assert(rotateStringRight("abcde", 3) == "cdeab")
    assert(rotateStringRight("abcde", 4) == "bcdea")
    assert(rotateStringRight("abcde", 5) == "abcde")
    assert(rotateStringRight("abcde", 25) == "abcde")
    assert(rotateStringRight("abcde", 28) == "cdeab")
    print("Passed!")

def testSameChars():
    print("Testing sameChars()...", end="")
    assert(sameChars("abcabcabc", "cba") == True)
    assert(sameChars("cba", "abcabcabc") == True)
    assert(sameChars("abcabcabc", "cbad") == False)
    assert(sameChars("abcabcabc", "cBa") == False)
    assert(sameChars(42,"The other parameter is not a string") == False)
    assert(sameChars("","") == True)
    assert(sameChars("","a") == False)
    print("Passed!")

def testMostFrequentLetters():
    print("Testing mostFrequentLetters()...", end="")
    assert(mostFrequentLetters("Cat") == 'ACT')
    assert(mostFrequentLetters("A cat") == 'A')
    assert(mostFrequentLetters("A cat in the hat") == 'AT')
    assert(mostFrequentLetters("This is a test") == 'ST')
    assert(mostFrequentLetters("This is an I test?") == 'IST')
    assert(mostFrequentLetters("") == "")
    print("Passed!")

def testWordWrap():
    print("Testing wordWrap()...", end="")
    assert(wordWrap("abcdefghij", 4) == """\
abcd
efgh
ij""")
    assert(wordWrap("a b c de fg", 4) == """\
a*b
c*de
fg""")
    print("Passed!")

def testLargestNumber():
    print("Testing largestNumber()...", end="")
    assert(largestNumber("I saw 3") == 3)
    assert(largestNumber("3 I saw!") == 3)
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    assert(largestNumber("I saw 3 dogs, 1700 cats, and 14 cows!") == 1700)
    assert(largestNumber("One person ate two hot dogs!") == None)
    print("Passed!")

def testLongestSubpalindrome():
    print("Testing longestSubpalindrome()...", end="")
    assert(longestSubpalindrome("ab-4-be!!!") == "b-4-b")
    assert(longestSubpalindrome("abcbce") == "cbc")
    assert(longestSubpalindrome("aba") == "aba")
    assert(longestSubpalindrome("a") == "a")
    print("Passed!")

def testLeastFrequentLetters():
    print("Testing leastFrequentLetters()...", end="")
    assert(leastFrequentLetters("abc def! GFE'cag!!!") == "bd")
    assert(leastFrequentLetters("abc def! GFE'cag!!!".lower()) == "bd")
    assert(leastFrequentLetters("abc def! GFE'cag!!!".upper()) == "bd")
    assert(leastFrequentLetters("") == "")
    assert(leastFrequentLetters("\t \n&^#$") == "")
    noq = string.ascii_lowercase.replace('q','')
    assert(leastFrequentLetters(string.ascii_lowercase + noq) == "q")
    print("Passed!")

def testAreAnagrams():
    print("Testing areAnagrams()...", end="")
    assert(areAnagrams("", "") == True)
    assert(areAnagrams("abCdabCd", "abcdabcd") == True)
    assert(areAnagrams("abcdaBcD", "AAbbcddc") == True)
    assert(areAnagrams("abcdaabcd", "aabbcddcb") == False)
    print("Passed!")

def testCollapseWhitespace():
    print("Testing collapseWhitespace()...", end="")
    assert(collapseWhitespace("a\n\n\nb") == "a b")
    assert(collapseWhitespace("a\n   \t    b") == "a b")
    assert(collapseWhitespace("a\n   \t    b  \n\n  \t\t\t c   ") ==
                              "a b c ")
    print("Passed!")

def testReplace():
    print("Testing replace()...", end="")
    (s1, s2, s3) = ("abcde", "ab", "cd")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("abcdeabcde", "ab", "cd")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("babababa", "ab", "cd")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("abb", "ab", "a")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("", "ab", "a")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("abc", "", "q")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    (s1, s2, s3) = ("abc", "ab", "")
    assert(replace(s1, s2, s3) == s1.replace(s2, s3))
    print("Passed!")

def testEncodeOffset():
    print("Testing encodeOffset()...", end="")
    assert(encodeOffset("ACB", 1) == "BDC")
    assert(encodeOffset("ACB", 2) == "CED")
    assert(encodeOffset("XYZ", 1) == "YZA")
    assert(encodeOffset("ABC", -1) == "ZAB")
    assert(encodeOffset("ABC", -27) == "ZAB")
    assert(encodeOffset("Abc", -27) == "Zab")
    assert(encodeOffset("A2b#c", -27) == "Z2a#b")
    print("Passed!")

def testDecodeOffset():
    print("Testing decodeOffset()...", end="")
    assert(decodeOffset("BDC", 1) == "ACB")
    assert(decodeOffset("CED", 2) == "ACB")
    assert(decodeOffset("YZA", 1) == "XYZ")
    assert(decodeOffset("ZAB", -1) == "ABC")
    assert(decodeOffset("ZAB", -27) == "ABC")
    assert(decodeOffset("Zab", -27) == "Abc")
    assert(decodeOffset("Z2a#b", -27) == "A2b#c")
    print("Passed!")

def testEncrypt():
    print("Testing encrypt()...", end="")
    assert(encrypt("Go Team!", "azby") == "GNUCAL")
    assert(encrypt("a1m2a3z4i5n6g !?!?", "yes") == "YQSXMFE")
    assert(encrypt("", "wow") == "")
    assert(encrypt("Wow!", "AZBY") == "password must be all lowercase")
    print("Passed!")

def testDecrypt():
    print("Testing decrypt()...", end="")
    assert(decrypt("GNUCAL", "azby") == "GOTEAM")
    assert(decrypt("YQSXMFE", "yes") == "AMAZING")
    assert(decrypt("", "wow") == "")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testDigitCount()
    testHasConsecutiveDigits() 
    testGcd()
    testPi()
    testH()
    testEstimatedPi()
    testEstimatedPiError()
    testNthAdditivePrime()
    testNthPerfectNumber() 
    testVowelCount()
    testInterleave()
    testHasBalancedParentheses()
    testLongestDigitRun()
    testLongestIncreasingRun()
    testNthPalindromicPrime()
    testNthLeftTruncatablePrime()
    testNthCarolPrime()
    testSumOfSquaresOfDigits()
    testRotateStringLeft()
    testRotateStringRight()
    testWordWrap()
    testLargestNumber()
    testIsHappyNumber()
    testNthHappyNumber()
    testNthHappyPrime()
    testMostFrequentDigit()
    testNthPowerfulNumber()
    testNthCircularPrime()
    testFindZeroWithBisection()
    testLongestSubpalindrome()
    testLeastFrequentLetters()
    testSameChars()
    testMostFrequentLetters()
    testAreAnagrams()
    testCollapseWhitespace()
    testReplace()
    testEncodeOffset()
    testDecodeOffset()
    testEncrypt()
    testDecrypt()

def main():
    cs112_s18_week2_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()

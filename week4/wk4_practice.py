#################################################
# Hw4
#################################################

import cs112_s18_week4_linter
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
# Hw4 problems
#################################################


#Code Tracing

def onesDigit(n):
    return n%10

def ct1(L):
    # loop through list and accumulate the sum(L) and the max(L)
    # for each index
    for i in range(len(L)):
        L[i] += sum(L) + max(L)
    return sorted(L, key=onesDigit)
# a = [2,1,0]
# print(ct1(a))
# print(a)

def ct2(a, b): # a = [4], b = [2, 3]
    # += destructively modifies the list
    a += [3] # a = [3, 4]
    a = a + [4] # NEW LIST: a = [4, 3, 4]
    for c in a: # for each item in a
        # 1. 4
            # a = 2; b = [6, 3]
            # b = 3; NEW b = [6, 3, 4]
        # 2. 3
            # a = 9; NEW b = [9, 3, 4, 3]
            # b = 3; b = [9, 3, 4, 3]
            # c = 4; b = [9, 3, 4, 3, 3]
        # 3. 4
            # a = 9; NEW b = [9, 3, 4, 3, 3]
            # b = 3; b = [13, 3, 4, 3, 3, 4]
            # c = 4; n/a
            # d = 3; n/a
            # e = 4; n/a
        for i in range(len(b)):
            if (b[i] not in a):
                print("A", end="")
                b[i] += c # += destructively modifies the list
            elif (c % 2 == 1):
                print("B", end="")
                b += [c] # += destructively modifies the list
            elif (b[-1] != c):
                print("C", end="")
                b = b + [c] # creates a NEW list
    return (a,b)
# a = [4]
# b = [2,3]
# print(ct2(a,b))
# print(a,b)

def ct3(L):
    result = [ ]
    # list comprehension exponentially raise each item by the index
    # M =  [2, 50, 300]
    M = [L[i]*10**i for i in range(len(L))]
    for val in M:
        result.extend([val, L.pop()])
        # pop removes elements from the end of L
        # [2, 3, 50, 5, 300, 2]
    return result
# L = [2,5,3]
# M = ct3(L)

def ct4(L):
    result = [ ]
    M = L[:] # same as M = copy.copy(L)
    if (M == L): result.append(1)
    if (M is L): result.append(2)
    if (M[0] == L[0]): result.append(3) #[1, 3]
    if (M[0] is L[0]): result.append(4) #[1, 3, 4]
    return result
# print(ct4([5,7,6]))

def ct5(L):
    M = L #aliased
    L += [4] # [0, 4]
    M = M + [5] # new list [0, 4, 5]
# ct5(list(range(1)))

#  Reasoning Over Code
def rc1(M):
    # M must be a list and length 5
  assert(isinstance(M,  list) and (len(M) ==  5))
    # i = -1 0 1 2
  for i in range(-1, 3):
    assert(M[i] == M[i-1] + i)
  return  (sum(M) ==  15)
# rc1([2, 3, 5, 3, 2])

def rc2(L):
  assert((isinstance(L, list)) and (None not in L))
  i = 0
  while (L[i] !=  None):
    j = L[i]
    L[i] = None
    i = j
    a = [None]*2
    # a = [None, None, -1, None, None]
  return  (L  == a + [-1] + a)
#  rc2([1, 3, -1, 4, 0])

def alternatingSum(a):
    total = a[0]
    length = len(a)
    if length == 0: return 0
    if length == 1: return a[0]

    for i in range(1, length):
        if i % 2 == 0:
            total += a[i]
        else:
            total -= a[i]
    return total

def median(a):
    length = len(a)
    if length == 0: return 0
    if length == 1: return a[0]

    tmp = a[:]
    tmp.sort()
    med = int(roundHalfUp(length/2))
    if length % 2 == 1:
        return tmp[med - 1]
    else:
        return ((tmp[med] +
                 tmp[med - 1]) / 2)

def isPalindromicList(a):
    if len(a) == 0 or len(a) == 1: return True
    return a == a[::-1]

def reverse(a):
    size = len(a)
    hiindex = size - 1
    iters = size // 2 # number of iters required
    for i in range(0, iters):
        (a[hiindex], a[i]) = (a[i], a[hiindex])
        hiindex -= 1

def vectorSum(a, b):
    tmp = [None] * len(a)

    for i in range(len(a)):
        tmp[i] = a[i] + b[i]
    return tmp

def isSorted(a):
    if len(a) == 0 or len(a) == 1: return True
    sortedList = a.sort()
    return a == sortedList

def dotProduct(a, b):
    tmp = [None] * len(a)

    for i in range(len(a)):
        tmp[i] = a[i] * b[i]
    return sum(tmp)

def check_sublist(a1, a2):
    if len(a1) < len(a2): return False
    j = 0

    for i in range(len(a1)):
        if a1[i] == a2[j]:
            j += 1
        else:
            j = 0
        # if all characters in a2 match
        if j == len(a2): return True

    return j == len(a2)

def isRotation(a1, a2):
    size1 = len(a1)
    size2 = len(a2)

    if size1 != size2: return False
    # concat first string with itself
    doubleArray = a1 + a1
    return check_sublist(doubleArray, a2)

def nondestructiveRotateList(a, n):
    if n == 0: return a
    rotated = a[-n:] + a[:-n]
    return rotated


def destructiveRotateList(a, n):
    if n == 0: return a
    length = len(a)
    a += [a[(i - n) % len(a)] for i in a]
    del a[:length]

def moveToBack(a, b):
    for num in b:
        if num in a:
            count = a.count(num)
            for i in range(count):
                idx = a.index(num)
                del a[idx]
                a.append(num)
    return a

def binaryListToDecmial(a):
    decimal = 0
    rev = a[::-1]

    for i in range(len(a)):
        if rev[i] == 1:
            decimal += 2**i
    return decimal

def smallestDifference(a):
    if len(a) == 0: return -1
    if len(a) == 2: return abs(a[0] - a[1])
    arr = sorted(a)
    minDiff = 10**20

    for i in range(len(arr) - 1):
        if (abs(arr[i + 1] - arr[i]) < minDiff):
                minDiff = abs(arr[i + 1] - arr[i])

    return minDiff

def split(s, delimiter):
    if delimiter not in s: return [s]
    arr = []
    tmp = ""
    for i in range(len(s)):
        if s[i] != delimiter:
            tmp += s[i]
        elif s[i] == delimiter:
            arr.append(tmp)
            tmp = ""
    arr.append(tmp)
    return arr

def join(L, delimiter):
    tmp = ""

    for c in L:
        if c != L[-1]:
            tmp += c + delimiter
        else:
            tmp += c
    return tmp

def repeatingPattern(a):
    storage = []
    # lengths from 1 to half the list's length
    for length in range(1, len(a) // 2 + 1):
        # generate a my_dict of all sub-lists of size length
        for start in range(0, len(a) - length + 1):
            storage.append(a[start:start + length])

    for c in storage:
        count = storage.count(c)
        if a == count * c:
            return True
    return False

def normalize(word):
    word = word.strip().lower() # sanitize it
    word = ''.join(sorted(word))
    return word

from collections import Counter

def mostAnagrams(wordList):
    anagrams = []
    for i in range(len(wordList)):
        # Counter checks the number of times each letter appears in each word
        counter_word = Counter(wordList[i])
        for j in range(i+1, len(wordList)):
            other_word = wordList[j]
            if Counter(other_word) == counter_word:
                anagrams.append(other_word)
    anagrams.sort()

    return anagrams[0]
#mostAnagrams(['carets', 'pass', 'stop',
# 'crates', 'reacts', 'recast', 'traces'])

def plus3(x):
    return (x+3)

def map(f, a):
    solution = []

    for item in a:
        solution.append(f(item))
    return solution

def fibonacci(n):
    if n < 0:
        return -1
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def firstNEvenFibonacciNumbers(n):
    arr = []
    count = 0
    test = 2

    while count < n:
        tmp = fibonacci(test)
        if tmp % 2 == 0:
            arr.append(tmp)
            count += 1
        test += 1
    return arr

def mostCommonName(a):
    count = []
    solution = []
    maxNum = -1

    for name in a:
        count.append(a.count(name))
    for num in count:
        maxNum = max(maxNum, num)

    for i in range(len(count)):
        if count[i] == maxNum and a[i] not in solution:
            solution.append(a[i])

    if len(solution) == 1:
        return solution[0]
    else:
        return sorted(solution)

def histogram(a):
    hist = ['60-69:', '70-79:', '80-89:', '90++ :' ]
    counts = [0]*4
    solution = ''
    for grade in a:
        if grade >= 60 and grade < 70:
            counts[0] += 1
        elif grade >= 70 and grade < 80:
            counts[1] += 1
        elif grade >= 80 and grade < 90:
            counts[2] += 1
        elif grade > 90:
            counts[3] += 1

    for i in range(len(counts)):
        stars = '*' * counts[i]
        solution += hist[i] + ' ' + stars + '\n'

    return solution

def nearestWords(wordList, word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    solution = []
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in splits for c in letters if b]
    inserts = [a + c + b for a, b in splits for c in letters]

    words = deletes + transposes + replaces + inserts

    for item in wordList:
        if item in words:
            solution.append(item)
    return solution

def bowlingScore(pinsPerThrowList):
    total = 0
    frame = 0
    idx = 0
    while frame < 10:
        # "strike"
        # the number of pins in the next two throws are added to the score.
        if pinsPerThrowList[idx] == 10:
            total += pinsPerThrowList[idx] + sum(pinsPerThrowList[idx+1:idx+3])
            idx += 1
        # "spare"
        # the number of pins knocked down in the next
        # throw are added to the score.
        elif sum(pinsPerThrowList[idx:idx+2]) == 10:
            total += sum(pinsPerThrowList[idx:idx+3])
            idx += 2
        # if there is a spare or strike in the final frame,
        # then the bowler gets one extra throw in that frame
        # (but if there is a subsequent strike,
        # they still get only that one extra throw)
        elif frame == 10 and pinsPerThrowList[idx] == 10:
            total += pinsPerThrowList[idx:idx+3]
            return total
        elif frame == 10 and sum(pinsPerThrowList[idx:idx+1]) == 10 \
                and pinsPerThrowList[idx+2]:
            total += sum(pinsPerThrowList[idx:idx+3])
            return total
        else:
            total += sum(pinsPerThrowList[idx:idx+2])
            idx += 2
        frame += 1

    return total

def evalPolynomial(coeffs, x):
    expon = len(coeffs) - 1
    total = 0

    for i in coeffs:
        total += i * x ** expon
        expon -= 1
    return total

def multiplyPolynomials(p1, p2):
    solution = []
    for i in p1:
        for j in p2:
            temp = j * i
            if temp > 0:
                solution.append(temp)
    return solution

def polynomialToString(p):
    varName = 'n'
    exponentiation = '^'
    solution = ''
    sign = ''
    exponNum = len(p) - 1

    for item in p:
        temp = 0
        if item == p[0]:
            temp = str(item)
            solution += temp + varName + exponentiation + \
                        str(exponNum) + ' '
        elif item < 0:
            sign = '- '
            temp = -item
            solution += sign + str(temp) + varName + \
                        exponentiation + str(exponNum) + ' '
        elif item == 0:
            continue
        elif exponNum == 1 and item > 0:
            sign = '+ '
            temp = str(item)
            solution += sign + temp
        elif exponNum == 1 and item < 0:
            sign = '- '
            temp = str(item)
            solution += sign + temp
        else:
            sign = '+ '
            temp = str(item)
            solution += sign + temp + varName + \
                        exponentiation + str(exponNum) + ' '
        exponNum -= 1
    return solution

def areaOfPolygon(L):
    return 42

#################################################
# Hw4 Test Scripts
#################################################

def testAlternatingSum():
    print("testing alternatingSum()...", end="")
    assert (alternatingSum([1]) == 1)
    assert (alternatingSum([0]) == 0)
    assert (alternatingSum([5, 3, 8, 4]) == 6)
    assert (alternatingSum([1, 3, 6]) == 4)

def testMedian():
    print("Testing median()...", end="")
    assert (median([1]) == 1)
    assert (median([]) == 0)
    assert (median([1, 5, 4, 4]) == 4)
    assert (median([1, 6, 2, 7, 15]) == 6)
    print("Passed!")

def testIsPalindromicList():
    print("Testing isPalindromiclist()...", end="")
    assert (isPalindromicList([1]) == True)
    assert (isPalindromicList([]) == True)
    assert (isPalindromicList([1, 2, 1]) == True)
    assert (isPalindromicList([1, 6, 2, 7, 15]) == False)
    print("Passed!")

def testVectorSum():
    print("Testing vectorSum()...", end="")
    assert (vectorSum([1], [1]) == [2])
    assert (vectorSum([2, 4], [20, 30]) == [22, 34])
    print("Passed!")

def testisSorted():
    print("Testing isSorted()...", end="")
    assert (isSorted([1]) == True)
    assert (isSorted([2, 1]) == False)
    print("Passed!")

def testdotProduct():
    print("Testing dotProduct()...", end="")
    assert (dotProduct([1], [1]) == 1)
    assert (dotProduct([1,2,3], [4,5,6] ) == 32)
    print("Passed!")

def testisRotation():
    print("Testing isRotation()...", end="")
    assert (isRotation([1], [1]) == True)
    assert (isRotation([1], [1, 2]) == False)
    assert (isRotation([2,3,4,5,6], [4,5,6,2,3]) == True)
    print("Passed!")

def testnondestructiveRotateList():
    print("Testing nondestructiveRotateList()...", end="")
    assert (nondestructiveRotateList([1, 2, 3, 4], 1) == [4, 1, 2, 3])
    assert (nondestructiveRotateList([4, 3, 2, 6, 5], 2) == [6, 5, 4, 3, 2])
    assert (nondestructiveRotateList([1, 2, 3], 0) == [1, 2, 3])
    assert (nondestructiveRotateList([1, 2, 3], -1) == [2, 3, 1])
    print("Passed!")

def testMoveToBack():
    print("Testing moveToBack()...", end="")
    assert(moveToBack([2, 3, 3, 4, 1, 5], [3]) == [2, 4, 1, 5, 3, 3])
    assert(moveToBack([2, 3, 3, 4, 1, 5], [2, 3]) == [4, 1, 5, 2, 3, 3])
    assert(moveToBack([2, 3, 3, 4, 1, 5], [3, 2]) == [4, 1, 5, 3, 3, 2])
    print("Passed!")

def testBinaryListToDecimal():
    print("Testing binaryListToDecmial()...", end="")
    assert(binaryListToDecmial([1, 0]) == 2)
    assert(binaryListToDecmial([1, 0, 1, 1]) == 11)
    assert(binaryListToDecmial([1, 1, 0, 1]) == 13)
    print("Passed!")

def testSmallestDifference():
    print("Testing smallestDifference()...", end="")
    assert (smallestDifference([1, 5, 3, 19, 18, 25] ) == 1)
    assert (smallestDifference([30, 5, 20, 9]) == 4)
    assert (smallestDifference([]) == -1)
    print("Passed!")

def testSplit():
    print("Testing split()...", end="")
    assert (split("ab,cd,efg", ",") == ["ab", "cd", "efg"])
    assert (split("this-is-a-test", "-") == ["this", "is", "a", "test"])
    print("Passed!")

def testJoin():
    print("Testing join()...", end="")
    assert(join(["ab", "cd", "efg"], ",") == "ab,cd,efg")
    print("Passed!")

def testRepeatingPatterns():
    print("Testing repeatingPattern()...", end="")
    assert(repeatingPattern([1, 2, 3, 1, 2, 3]) == True)
    print("Passed!")

def testMap():
    print("Testing map()...", end="")
    assert (map(plus3, [2,4,7]) == [5,7,10])
    print("Passed!")

def testfirstNEvenFibonacciNumbers():
    print("Testing firstNEvenFibonacciNumbers()...", end="")
    assert (firstNEvenFibonacciNumbers(4) == [2, 8, 34, 144])
    print("Passed!")

def testMostCommonName():
    print("Testing mostCommonName()...", end="")
    assert(mostCommonName(['Jane', 'Aaron', 'Cindy', 'Aaron']) == "Aaron")
    assert(mostCommonName(['Jane', 'Aaron', 'Jane', 'Cindy', 'Aaron'])
           == ['Aaron', 'Jane'])
    print("Passed!")

def testbowlingScore():
    print("Testing mostCommonName()...", end="")
    assert(bowlingScore([10, 10, 10, 10, 10, 10,
                         10, 10, 10, 10, 10, 10]) == 300)
    assert(bowlingScore([1, 4, 4, 5, 6, 4, 5, 5,
                         10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6]) == 133)
    print("Passed!")

def testevalPolynomial():
    print("Testing evalPolynomial()...", end="")
    assert(evalPolynomial([2,3,0,4], 4) == 180)
    print("Passed!")

def testmultiplyPolynomials():
    print("Testing evalPolynomial()...", end="")
    assert(multiplyPolynomials([2, 0, 3], [4, 5]) == [8, 10, 12, 15])
    print("Passed!")

def testpolynomialToString():
    print("Testing polynomialToString()...", end="")
    assert(polynomialToString([2, -3, 0, 4]) == "2n^3 - 3n^2 + 4")
    print("Passed!")

#################################################
# Hw4 Main
#################################################

def testAll():
    testAlternatingSum()
    testMedian()
    testIsPalindromicList()
    testVectorSum()
    testisSorted()
    testdotProduct()
    testisRotation()
    testnondestructiveRotateList()
    testMoveToBack()
    testBinaryListToDecimal()
    testSmallestDifference()
    testSplit()
    testJoin()
    testMap()
    testfirstNEvenFibonacciNumbers()
    testMostCommonName()
    testbowlingScore()
    testpolynomialToString()

def main():
    cs112_s18_week4_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
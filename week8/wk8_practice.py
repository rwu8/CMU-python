#################################################
# Week8 Practice
#################################################
import string
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

# Big - O Analysis: Problems and Solutions
# Find the Big - O runtime of the given function
# by computing the runtime of each line.

# Big O - ignore all lower-order terms and constants

import string
# Problem 1
def foo(L):  # L is a list
    i = 1
    listLength = len(L)
    result = []
    while i < listLength:
        result += L[i]
        i *= 3
    return i
# Overall - O(logn)


# Problem 2
def foo(S):  # S is a string
    stringLength = len(S)
    i = stringLength
    result = {}
    while i > 0:
        result.add(S[i])
        i //= 3
    return result
# Overall - O(log(n))

# Problem 3
def foo(L):  # L is a list
    lenList = len(L)
    count = 0
    for i in range(lenList):
        for j in range(lenList):
            count += L[i]
    return count
# Overall - O(n^2)

# Problem 4
def foo(s):  # s is a string of length N
    result = 0
    for char in string.ascii_lowercase:
        if char in s:
            s = s[1:]
            result += 1
    return result
# Overall - O(n)

# Problem 5
def foo(s):
    return len(s)
# Overall - O(1)

# Problem 6
def foo(L):  # L is a list
    n = len(L)
    for i in range(n ** 2, n ** 3, n):
        L.append(i)
    for j in range(n // 5, n // 2, n // 10):
        L.pop()
    return L
# Overall - O(n^2)

# Problem 7
def foo(L):
    result = []
    for i in range(1, len(sorted(L)) + 1): # O(nlog(n)) + n iterations
        newList = len(L) * [i] # O(n^2)
        result.extend(newList) # result has length O(n^2)
    return sorted(result) # n^2 log(n^2)
# Overall - O(n^2 log(n))

# Problem 8
def foo(L):  # L is a square, 2D list
    n = len(L)
    j = 1
    count = 0
    while j < n: # O(logn)
        for i in range(n): #O(n)
            if max(L[j]) in L[i]: #O(n)
                count += 1 # O(1)
        j *= 2
    return count
# Overall - O(n^2 log(n))

# Problem 9
def bigOh(L):
    new = list()
    for i in range(len(L)): # n times
        new.extend(L[:i:2])
    new.sort() # nlog(n)
    result = set(new) # O(n^2)
    return result
# Overall - O(n^2 log(n))


def mostCommonName(L):
    if L == []: return None
    d = dict()
    common = set()
    maxNum = 0

    for name in L:
        d[name] = d.get(name, 0) + 1
        maxNum = max(maxNum, d[name])

    for k in d:
        if d[k] == maxNum:
            common.add(k)

    if len(common) == 1:
        return list(common)[0]
    return common


# You should write two different versions, one that runs in O(n**2) and the other in O(n)
# O(n^2)
# def getPairSum(a, target):
#     if len(a) == 1: return []
#     solution = []
#     for i in range(len(a)):
#         for j in range(len(a)):
#             if a[i] + a[j] == target and i != j:
#                 if [[a[i], a[j]]] in solution:
#                     break
#                 else:
#                     solution.append([a[i], a[j]])
#
#     if len(solution) > 0:
#         return solution[0]
#     else:
#         return []

# O(n)
def getPairSum(a, target):
    solution = []
    a.sort()
    l = 0
    r = len(a) - 1

    while l < r:
        if a[l] + a[r] < target:
            l += 1
        elif a[l] + a[r] > target:
            r -= 1
        else:
            solution.append([a[l], a[r]])
            l += 1
            r -= 1

    if len(solution) > 0:
        return solution[0]
    else:
        return []

def mergeWithOneAuxList(aux, a, start1, start2, end):
    index1 = start1
    index2 = start2
    length = end - start1
    for i in range(length):
        if ((index1 == index2) or
                ((index2 != end) and (a[index1] > a[index2]))):
            aux[start1 + i] = a[index2]
            index2 += 1
        else:
            aux[start1 + i] = a[index2]
            index2 += 1

def mergeSortWithOneAuxList(a):
    n = len(a)
    aux = [None] * n
    step = 1

    while step < n:
        for start1 in range(0,n,2*step):
            start2 = min(start1 + step, n)
            end = min(start1 + 2*step, n)
            mergeWithOneAuxList(aux, a, start1, start2, end)
        for i in range(n):
            a[i] = aux[i]
        step *= 2


#################################################
# Test Functions
#################################################

def testMostCommonName():
    print("Testing mostCommonName()...", end="")
    assert(mostCommonName(["Jane", "Aaron", "Cindy", "Aaron"])
           == "Aaron")
    assert(mostCommonName(["Jane", "Aaron", "Jane", "Cindy", "Aaron"])
           == {"Aaron", "Jane"})
    assert(mostCommonName(["Cindy"]) == "Cindy")
    assert(mostCommonName(["Jane", "Aaron", "Cindy"])
           == {"Aaron", "Cindy", "Jane"})
    assert(mostCommonName([]) == None)
    print("Passed!")

def testGetPairSum():
    print("Testing getPairSum...", end="")
    assert(getPairSum([1],1) == [])
    assert(getPairSum([5, 2], 7) in [ [5, 2], [2, 5] ])

    # (can return [10, -8] or [-1,3] or [1,1])
    assert(getPairSum([10,-1,1,-8,3,1], 2) in [[10, -8], [-8, 10],
                                               [-1, 3], [3, -1],
                                               [1, 1]])

    assert(getPairSum([10,-1,1,-8,3,1], 10) == [])
    assert(getPairSum([1, 4, 3], 2) == [])
    print("Passed!")

def testAll():
    testGetPairSum()
    testMostCommonName()

def main():
    testAll()

if __name__ == '__main__':
    main()
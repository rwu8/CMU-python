#################################################
# Hw8
#################################################

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
# Hw8 problems
#################################################

# Big-O Calculation
def slow1(lst): # N is the length of the list lst
    assert(len(lst) >= 2)
    a = lst.pop() # O(1)
    b = lst.pop(0) #O(N)
    lst.insert(0, a) #O(N)
    lst.append(b) #O(1)
# Big O calculation: O(N)

def slow2(lst): # N is the length of the list lst
    counter = 0
    for i in range(len(lst)): #O(n)
        if lst[i] not in lst[:i]: #O(n)
            counter += 1 #O(1)
    return counter # O(1)
# Big O calculation: O(n^2)

import string
def slow3(s): # N is the length of the string s
    maxLetter = ""
    maxCount = 0
    for c in s: # O(n)
        for letter in string.ascii_lowercase: # O(27)
            if c == letter: # O(1)
                if s.count(c) > maxCount or \
                   s.count(c) == maxCount and c < maxLetter: # O(n)
                    maxCount = s.count(c) # O(n)
                    maxLetter = c # O(1)
    return maxLetter # O(1)
# Big O calculation: O(n^2)

def slow4(a, b): # a and b are lists with the same length N
    n = len(a) #O(n)
    assert(n == len(b))
    result = abs(a[0] - b[0])
    for c in a: # O(n)
        for d in b: # O(n)
            delta = abs(c - d) # O(1)
            if (delta > result):# O(1)
                result = delta# O(1)
    return result# O(1)
# Big O calculation: # O(n^2)

def movieAwards(oscarResults):
    d = dict()
    for item in oscarResults:
        for i in range(1, len(item)):
            d[item[1]] = 1 + d.get(item[1], 0)
    return d

def largestSumOfPairs(a):
    if len(a) <= 1: return None
    a.sort()
    r = 0
    largestSum = 0

    for i in range(len(a)):
        r = len(a) - 1
        while i < r and i != len(a):
            largestSum = max(largestSum, (a[i] + a[r]))
            r -= 1
    return largestSum

def swap(a, i, j):
    (a[i], a[j]) = (a[j], a[i])

# return a tuple of two values: the number of comparisons and the number of swaps.
def instrumentedBubbleSort(a):
    numOfComparisons = 0
    numOfSwaps = 0
    n = len(a)
    end = n
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, end):
            numOfComparisons += 1
            if (a[i - 1] < a[i]):
                swap(a, i-1, i)
                swapped = True
                numOfSwaps += 1
        end -= 1
    return (numOfComparisons, numOfSwaps)

def containsPythagoreanTriple(a):
    a.sort()

    for i in range(len(a)):
        for j in range(i, len(a)):
            if math.sqrt(a[i]**2 + a[j]**2) in a:
                return True

    return False

def instrumentedSelectionSort(a):
    numOfComparisons = 0
    numOfSwaps = 0
    n = len(a)
    for index in range(n):
        minIndex = index
        for i in range(index+1, n):
            numOfComparisons += 1
            if (a[i] < a[minIndex]):
                minIndex = i
        swap(a, index, minIndex)
        numOfSwaps += 1
    return (numOfComparisons, numOfSwaps)

def formatDataset(filename):
    d = {}
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        tmp = line.split(' ')
        tmp[1] = tmp[1].split('\n')[0]
        d[int(tmp[0])] = d.get(int(tmp[0]), ()) + (int(tmp[1][0]),)

    # print(d)
    return d

dataset = formatDataset('facebookSNAPDatasets/smallFaceBook.txt')

def friendsOfUser(id, friendData):
    if id in dataset:
        return friendData[id]
    else:
        return None

# print(friendsOfUser(881, dataset))

def mutualFriends(id1, id2, friendData):
    if id1 not in friendData or id2 not in friendData:
        return None

    d1 = friendData[id1]
    d2 = friendData[id2]

    mutualFriends = set()

    if len(d1) > len(d2):
        for k in d1:
            if k in d2:
                mutualFriends.add(k)
    else:
        for j in d2:
            if j in d1:
                mutualFriends.add(j)
    return mutualFriends
# print(mutualFriends(856,828,dataset))

d = { }
d["jon"] = set(["arya", "tyrion"])
d["tyrion"] = set(["jon", "jaime", "pod"])
d["arya"] = set(["jon"])
d["jaime"] = set(["tyrion", "brienne"])
d["brienne"] = set(["jaime", "pod"])
d["pod"] = set(["tyrion", "brienne", "jaime"])
d["ramsay"] = set()


def friendsOfFriends(d):
    new_dict = {}
    for k,v in d.items():
        new_dict[k] = set()
        for person in v:
            for friend in d[person]:
                if friend is not k and friend not in d[k]:
                    new_dict[k].add(friend)
    return new_dict

#################################################
# Test code is below here
#################################################

def testMovieAwards():
    print("Testing movieAwards()...", end="")
    assert (movieAwards({
    ("Best Picture", "The Shape of Water"),
    ("Best Actor", "Darkest Hour"),
    ("Best Actress", "Three Billboards Outside Ebbing, Missouri"),
    ("Best Director", "The Shape of Water"),
    ("Best Supporting Actor", "Three Billboards Outside Ebbing, Missouri"),
    ("Best Supporting Actress", "I, Tonya"),
    ("Best Original Score", "The Shape of Water")
  }) == {
    "Darkest Hour" : 1,
    "Three Billboards Outside Ebbing, Missouri" : 2,
    "The Shape of Water" : 3,
    "I, Tonya" : 1
  })
    print("Passed!")

def testLargestSumOfPairs():
    print("Testing largestSumOfPairs()...", end="")
    assert (largestSumOfPairs([8, 4, 2, 8]) == 16)
    assert (largestSumOfPairs([9, 3]) == 12)
    assert (largestSumOfPairs([]) == None)
    print('Passed!')

def testInstrumentedBubbleSort():
    print("Testing instrumentedBubbleSort()...", end="")
    assert(instrumentedBubbleSort([4, 6, 2, 8, 1, 6, 9, 3]) == (28, 15))
    assert(instrumentedBubbleSort([1,2,3,4,5,6,7,8]) == (8, 0))
    print('Passed!')

def testContainsPythagoreanTriple():
    print("Testing containsPythagoreanTriple()...", end="")
    assert (containsPythagoreanTriple([1, 3, 6, 2, 5, 1, 4]) == True)
    assert (containsPythagoreanTriple([1, 2, 3, 5, 7, 8]) == False)
    print('Passed!')

def testFriendsOfFriends():
    print("Testing friendsOfFriends()...", end="")
    assert (friendsOfFriends(d) == {
        'tyrion': {'arya', 'brienne'},
        'pod': {'jon'},
        'brienne': {'tyrion'},
        'arya': {'tyrion'},
        'jon': {'pod', 'jaime'},
        'jaime': {'pod', 'jon'},
        'ramsay': set()
    })
    print('Passed!')

def testAll():
    testMovieAwards()
    testLargestSumOfPairs()
    testContainsPythagoreanTriple()
    testFriendsOfFriends()
def main():
    testAll()

if __name__ == '__main__':
    main()
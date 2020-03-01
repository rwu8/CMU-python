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

def mystery(list):
    count = 0
    for value in list:
        if (value == 0):
            count += 1
    return count
# This function returns the number of 0's in a given list.

# 5 Reasoning About (Recursive) Code problems

def f(n):
   # assume n is a non-negative integer
   if (n < 10):
      return 1
   else:
      return 1 + f(n//10)
# This function counts the number of digits in a number

def f(a):
   # assume a is a list of strings
   if (len(a) == 0):
      return ""
   else:
      x = f(a[1:])
      if (len(x) > len(a[0])):
         return x
      else:
         return a[0]
# This function returns the first character in a string

def f(a):
   # assume a is a list of integers
   if (len(a) == 0):
      return 0
   elif (len(a) == 1):
      return (a[0] % 2)
   else:
      i = len(a)//2
      return f(a[:i]) + f(a[i:])
# This function divides and conquers the list and returns the sum of the list after modulo by 2

def f(n):
   # assume n is a non-negative integer
   if (n == 0):
      return 1
   else:
      return 2*f(n-1)
# This function returns 2^n

def f(n):
   # assume n is a non-negative integer
   if (n == 0):
      return 0
   else:
      return f(n-1) + 2*n - 1
# This function returns n squared

import os
def countFiles(path):
    count = 0
    # base case: file
    if not os.path.isdir(path):
        return 1
    # recursive case: folder
    for filename in os.listdir(path):
        count = count + countFiles(path + "/" + filename)
    return count

def permutations(a, k, depth=0):
    # returns a list of all permutations of the list a
    # print('  ' * depth, 'allPermutations(', a, k, ')')
    if (len(a) <= 1) or k <= 0:
        return [[]]
    else:
        allPerms = [ ]
        for i, item in enumerate(a):
            temp = a[:i] + a[i+1:]
            for subPermutation in permutations(temp, k - 1, depth + 1):
                allPerms += [[item] + subPermutation]
                # print('  ' * depth, '--> ', allPerms)
        return allPerms

#################################################
# Test Functions
#################################################

def testCountFiles():
    print("Testing countFiles()...", end="")
    assert (countFiles("sampleFiles/folderB/folderF/folderG") == 0)
    assert (countFiles("sampleFiles/folderB/folderF") == 0)
    assert (countFiles("sampleFiles/folderB") == 2)
    assert (countFiles("sampleFiles/folderA/folderC") == 4)
    assert (countFiles("sampleFiles/folderA") == 6)
    assert (countFiles("sampleFiles") == 10)
    print("Passed!")

def testPermutations():
    import itertools
    a = [1, 2, 3, 4]
    a_permutations = [list(x) for x in itertools.permutations(a, 2)]
    b = [x for x in range(30)]
    b_permutations = [list(x) for x in itertools.permutations(b, 2)]
    c = [x for x in range(72)]
    c_permutations = [list(x) for x in itertools.permutations(c, 2)]
    print("Testing countFiles()...", end="")
    assert(permutations(a, 2) == a_permutations)
    assert(permutations(b, 2) == b_permutations)
    assert (permutations(c, 2) == c_permutations)
    print("Passed!")

def testAll():
    testCountFiles()
    testPermutations()

def main():
    testAll()

if __name__ == '__main__':
    main()
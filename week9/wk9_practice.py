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

def countFiles(path):
    return 42


def permutations(a):
    # returns a list of all permutations of the list a
    if (len(a) == 0):
        return [[]]
    else:
        allPerms = []
        for subPermutation in permutations(a[1:]):
            for i in range(len(subPermutation) + 1):
                allPerms += [subPermutation[:i] + [a[0]] + subPermutation[i:]]
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

def testAll():
    testCountFiles()

def main():
    testAll()

if __name__ == '__main__':
    main()
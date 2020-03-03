#################################################
# Hw10
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
# Hw10 problems
#################################################

def getCourse(courseCatalog, courseNumber):
    parentCourse = courseCatalog[0]

    # base case
    if len(courseCatalog) <= 1:
        return None
    # found our course!
    elif courseCatalog[1] == courseNumber:
        return parentCourse + '.' + courseNumber

    # next element is a list
    elif isinstance(courseCatalog[1],list):
        subCourse = getCourse(courseCatalog[1], courseNumber)
        if subCourse:
            return parentCourse + '.' + subCourse
    # recursive case, delete subCourse element from search
    return getCourse([parentCourse] + courseCatalog[2:], courseNumber)




#################################################
# Test code is below here
#################################################

def testGetCourse():
    courseCatalog = ["CMU",
                         ["CIT",
                              ["ECE", "18-100", "18-202", "18-213"],
                              ["BME", "42-101", "42-201"],
                          ],
                         ["SCS",
                              ["CS",
                                   ["Intro", "15-110", "15-112"],
                                   "15-122", "15-150", "15-213"
                               ],
                          ],
                         "99-307", "99-308"
                     ]
    print('Testing getCourse()...', end=" ")
    assert (getCourse(courseCatalog, "18-100") == "CMU.CIT.ECE.18-100")
    assert (getCourse(courseCatalog, "15-112") == "CMU.SCS.CS.Intro.15-112")
    assert (getCourse(courseCatalog, "15-213") == "CMU.SCS.CS.15-213")
    assert (getCourse(courseCatalog, "99-307") == "CMU.99-307")
    assert (getCourse(courseCatalog, "15-251") == None)
    print('Passed!')

def testAll():
    testGetCourse()

def main():
    testAll()

if __name__ == '__main__':
    main()
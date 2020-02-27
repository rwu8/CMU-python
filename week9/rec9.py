###############################################################################
# --------------- 15-112 Recitation Week 9: OOP & Recursion ---------------- #

# This is a starter file of the problems we did in recitation. A good way to
# use this file is to try to re-write problems you saw in recitation from
# scratch. This way, you can test your understanding and ask on Piazza or
# office hours if you have questions :)

# --------------------------------------------------------------------------- #
###############################################################################
# Student Classes
###############################################################################
'''
define class(es) so that testStudentOOP will pass! Make sure to use inheritance
properly!
'''


class Student(object):
    students = []
    @staticmethod
    def getSchool():
        return "Carnegie Mellon"

    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.classes = set()
        self.addStudents(self.name)

    def addClass(self, course):
        self.classes.add(course)

    def addStudents(self, student):
        Student.students.append('Student named ' + self.name)

class OneTwelveStudent(Student):
    students = []
    def __init__(self, name, major, minor):
        super().__init__(name, major)
        self.minor = minor
        self.classes.add('15-112')
        self.grade = 42

    def get112Grade(self):
        return self.grade

    def study112(self):
        self.grade += 42

    def addStudents(self, student):
        Student.students.append('OneTwelveStudent named ' + self.name)
        OneTwelveStudent.students.append('OneTwelveStudent named ' + self.name)


def testStudentOOP():
    print("Testing Student Classes...", end="")
    chaya = Student("Chaya", "Comp Bio")
    chaya.addClass("76-100")

    kyle = OneTwelveStudent("Kyle", "IS", "JJ")
    kyle.addClass("76-100")

    assert(chaya.classes == set(['76-100']))
    assert(kyle.classes == set(['15-112', '76-100']))

    arman = Student("Arman", "ECE")
    kdchin = OneTwelveStudent("Kyle", "IS", "DD")

    assert(chaya != arman)
    assert(kyle != kdchin)
    assert(type(arman) == Student)
    assert(type(kyle) == OneTwelveStudent)
    assert(isinstance(kyle, Student))

    x = 5
    try:
        chaya.get112Grade()
    except:
        x = 4
    assert(x == 4)
    assert(kyle.get112Grade() == 42)
    kyle.study112()
    assert(kyle.get112Grade() == 42 + 42)

    # assert(sorted(str(Student.students)) == sorted(
    #     "{Student named Chaya, OneTwelveStudent named Kyle, Student named Arman, OneTwelveStudent named Kyle}"))
    # assert(sorted(str(OneTwelveStudent.students)) == sorted(
    #     "{OneTwelveStudent named Kyle, OneTwelveStudent named Kyle}"))

    assert(OneTwelveStudent.getSchool() == "Carnegie Mellon")
    print("Passed!")

testStudentOOP()

###############################################################################
# Recursive Reverse
###############################################################################
'''
Write the function reverse(s) using recursion (no loops fancy slicing!) in several
different ways:
1) Head and tail (reverse characters 1 to n-1, then put the first one at the end)
    "abcd" --> "a" "dcb" --> "dcba"
2) Split down the middle aka "divide and conquer" (reverse each half and combine)
    "abcd" --> "ba" "dc" --> "dcba"
3) With a stack trace!
'''

def reverseHeadTail(s, depth=0):
    print("   " * depth + "reverseHeadTail(" + str(s) + ")" )
    if len(s) == 1:
        return s
    else:
        print("   " * depth + "-->", s)
        return s[-1] + reverseHeadTail(s[:-1], depth + 1)

def reverseDivideAndConquer(s, depth=0):
    print("   " * depth + "reverseDivideAndConquer(" + str(s) + ")" )
    if len(s) == 0: return ""
    elif len(s) == 1:
        return s
    else:
        mid = len(s) // 2
        print("   " * depth + "-->", s)
        return reverseDivideAndConquer(s[mid:], depth + 1) + reverseDivideAndConquer(s[:mid], depth + 1)

def testReverse():
    print("Testing Reverse...")
    print("testing reverseHeadTail...", end=" ")
    assert (reverseHeadTail("abcd") == "dcba")
    print("Passed!")
    print("testing reverseDivideAndConquer...")
    assert (reverseDivideAndConquer("abcd") == "dcba")
    print("Passed!")

testReverse()
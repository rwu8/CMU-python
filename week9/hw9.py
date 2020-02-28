#################################################
# Hw9
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
# Hw9 problems
#################################################

def alternatingSum(lst, depth=0):
    # print("   " * depth + "alternatingSum(" + str(lst) + ")")
    if len(lst) == 0: return 0
    elif len(lst) == 1: return lst[0]
    # print("   " * depth + "-->", lst[0] - lst[1] + alternatingSum(lst[2:]))
    return  lst[0] - lst[1] + alternatingSum(lst[2:], depth + 1)

class VendingMachine(object):
    def __init__(self, items, price):
        self.items = items
        self.price = price
        self.paid = 0
        self.change = self.paid - self.price if self.paid > self.price else 0
        self.status = ""

    def __repr__(self):
        if self.items == 1:
            return "Vending Machine:<%d bottle; $%.2f each; $%d paid>" % (self.items, self.price / 100, self.paid)
        if self.paid == 0:
            return "Vending Machine:<%d bottles; $%.2f each; $%d paid>" % (self.items, self.price / 100, self.paid)
        return "Vending Machine:<%d bottles; $%.2f each; $%.2f paid>" % (self.items, self.price/100, self.paid/100)

    def getHashables(self):
        # return a tuple of hashables
        return (self.items, self.price)

    def __hash__(self):
        return hash(self.getHashables())

    def __eq__(self, other):
        return (isinstance(other, VendingMachine) and
                (self.items == other.items) and
                (self.price == other.price) and
                (self.paid == other.paid))

    def isEmpty(self):
        return self.items == 0

    def getBottleCount(self):
        return self.items

    def stillOwe(self):
        return self.price - self.paid

    # When the user inserts money, the machine returns a message about their
    # status and any change they need as a tuple.
    def insertMoney(self, money):
        self.paid += money
        formattedAmount = (self.price - self.paid) / 100

        if self.items == 0:
            self.status = "Machine is empty"
            temp = self.paid
            self.paid = 0

            return (self.status, temp)
        elif self.paid == 0:
            return self.price
        elif formattedAmount > 0:
            # if exact dollar amount
            if (self.price - self.paid) % 100 == 0:
                self.status = "Still owe $%d" % formattedAmount
            else:
                self.status = "Still owe $%.2f" % formattedAmount
        elif formattedAmount == 1.25:
            self.items -= 1
            self.status = "Got a bottle!"

        # otherwise we need to provide change
        else:
            self.items -= 1
            self.status = "Got a bottle!"
            self.paid = 0
            self.change = int(abs(formattedAmount) * 100)

        return (self.status, self.change)

    def stockMachine(self, items):
        self.items += items

class Bird(object):
    def __init__(self, type):
        self.type = type
        self.eggs = 0

    def __repr__(self):
        if self.eggs == 1:
            return self.type + " has 1 egg"
        else:            return self.type + " has " + str(self.eggs) + " eggs"

    def fly(self):
        return "I can fly!"

    def countEggs(self):
            return self.eggs

    def layEgg(self):
        self.eggs += 1
        return self.eggs

class Penguin(Bird):
    def fly(self):
        return "No flying for me."

    def swim(self):
        return "I can swim!"

class MessengerBird(Bird):
    def __init__(self, type, message=""):
        super().__init__(type)
        self.message = message

    def deliverMessage(self):
        return self.message

def generateCharacterString(s):
    if s == "": return 0
    if s[0] == s[1]:
        return s[0]

    # second character has a lower ordinal value
    elif ord(s[0]) > ord(s[1]):
        return s[0] + generateCharacterString([chr(ord(s[0]) - 1), s[1]])
    else:
        return s[0] + generateCharacterString([chr(ord(s[0]) + 1), s[1]])

def powersOf3ToN(n, depth=0):
    # print("   " * depth + "powersOf3ToN(" + str(n) + ")" )
    if n < 1: return None
    elif n == 1: return [1]
    elif n > 1 and n < 9: return ([1] + [3])

    n = int(n // 1)

    if almostEqual(3 ** int(roundHalfUp(math.log(n, 3))), n):
        # print("   " * depth + "-->", powersOf3ToN((n // 1) - 1, depth + 1) + [n])
        return powersOf3ToN((n // 1) - 1, depth + 1) + [n]
    else:
        return powersOf3ToN((n // 1) - 1, depth + 1)

class Polynomial(object):
    def __init__(self, coeffs):
        self.coeffs = [None] * len(coeffs)
        if coeffs == []:
            self.coeffs = [0]
        if isinstance(coeffs, str):
            self.coeffs = None
        elif len(coeffs) > 1 and coeffs[0] == 0:
            idx = 0
            while coeffs[idx] == 0 and idx < len(coeffs) - 1:
                idx += 1
                self.coeffs = list(coeffs[idx:])
        else:
            self.coeffs = coeffs

    def __repr__(self):
        return "Polynomial(coeffs=" + str(self.coeffs) + ")"

    def getHashables(self):
        # return a tuple of hashables
        return (tuple(self.coeffs))

    def __hash__(self):
        return hash(self.getHashables())

    def __eq__(self, other):
        if self.coeffs == []:
            return ([0] == other.coeffs)

        elif len(self.coeffs) == 1:
            return self.coeffs[0] == other
        else:
            return (isinstance(other, Polynomial) and (self.coeffs == other.coeffs))

    def degree(self):
        return self.coeffs[0]

    def coeff(self, index):
        return self.coeffs[len(self.coeffs) - 1 - index]

    def evalAt(self, num):
        if len(self.coeffs) == 2:
            return self.coeffs[0] * num + self.coeffs[1]
        else:
            return self.coeffs[0]*num**2 + self.coeffs[1] * num + self.coeffs[2]

    def scaled(self, scale):
        newCoeffs = [None] * len(self.coeffs)
        for index in range(len(self.coeffs)):
            newCoeffs[index] = self.coeffs[index] * scale
        return Polynomial(newCoeffs)

    # return a new polynomial that is the derivative
    # of the original, using the power rule:
    # More info: https://www.mathsisfun.com/calculus/power-rule.html
    def derivative(self):
        return Polynomial([2*self.coeffs[0], self.coeffs[1]])

    def addPolynomial(self, polynomial):
        if isinstance(polynomial, str): return None

        arr = list(polynomial.coeffs)

        if len(arr) < len(self.coeffs):
            while len(arr) < len(self.coeffs):
                arr = [0] + arr
        for index in range(len(self.coeffs)):
            arr[index] = self.coeffs[index] + arr[index]

        return Polynomial(arr)

    def multiplyPolynomial(self, polynomial):
        arr = [0] * (len(self.coeffs) + len(polynomial.coeffs) - 1)

        for o1, i1 in enumerate(self.coeffs):
            for o2, i2 in enumerate(polynomial.coeffs):
                arr[o1 + o2] += i1 * i2
        return Polynomial(arr)

class Quadratic(Polynomial):
    def __init__(self, coeffs):
        if len(coeffs) != 3:
            Quadratic(False)
        else:
            super().__init__(coeffs)

    def __repr__(self):
        return "Quadratic(a=%d, b=%d, c=%d" % (self.coeffs[0], self.coeffs[1], self.coeffs[2]) + ")"

    def discriminant(self):
        return self.coeffs[1]**2 - 4*self.coeffs[0]*self.coeffs[2]

    def numberOfRealRoots(self):
        discrim = self.discriminant()
        if discrim > 0:
            return 2
        elif discrim == 0:
            return 1
        else:
            return 0

    def getRealRoots(self):
        roots = self.numberOfRealRoots()
        if roots == 0:
            return []
        elif roots == 1:
            root = (-self.coeffs[1] + math.sqrt(self.discriminant())) / (2 * self.coeffs[0])
            return [root]
        else:
            root1 = (-self.coeffs[1] - math.sqrt(self.discriminant())) / (2 * self.coeffs[0])
            root2 = (-self.coeffs[1] + math.sqrt(self.discriminant())) / (2 * self.coeffs[0])
            return [root1, root2]

#################################################
# Test code is below here
#################################################

def testAlternatingSum():
    print("Testing alternatingSum()...", end="")
    assert(alternatingSum([1,2,3,4,5]) == 3)
    assert(alternatingSum([]) == 0)
    assert (alternatingSum([1,2,3,4,5,6]) == -3)
    print("Passed!")

def testVendingMachineClass():
    print("Testing Vending Machine class...", end="")
    # Vending machines have three main properties:
    # how many bottles they contain, the price of a bottle, and
    # how much money has been paid. A new vending machine starts with no
    # money paid.
    vm1 = VendingMachine(100, 125)
    assert (str(vm1) == "Vending Machine:<100 bottles; $1.25 each; $0 paid>")
    assert (vm1.isEmpty() == False)
    assert (vm1.getBottleCount() == 100)
    assert (vm1.stillOwe() == 125)

    # When the user inserts money, the machine returns a message about their
    # status and any change they need as a tuple.
    assert (vm1.insertMoney(20) == ("Still owe $1.05", 0))
    assert (str(vm1) == "Vending Machine:<100 bottles; $1.25 each; $0.20 paid>")
    assert (vm1.stillOwe() == 105)
    assert (vm1.getBottleCount() == 100)
    assert (vm1.insertMoney(5) == ("Still owe $1", 0))

    # When the user has paid enough money, they get a bottle and
    # the money owed resets.
    assert (vm1.insertMoney(100) == ("Got a bottle!", 0))
    assert (vm1.getBottleCount() == 99)
    assert (vm1.stillOwe() == 125)
    assert (str(vm1) == "Vending Machine:<99 bottles; $1.25 each; $0 paid>")

    # If the user pays too much money, they get their change back with the
    # bottle.
    assert (vm1.insertMoney(500) == ("Got a bottle!", 375))
    assert (vm1.getBottleCount() == 98)
    assert (vm1.stillOwe() == 125)

    # Machines can become empty
    vm2 = VendingMachine(1, 120)
    assert (str(vm2) == "Vending Machine:<1 bottle; $1.20 each; $0 paid>")
    assert (vm2.isEmpty() == False)
    assert (vm2.insertMoney(120) == ("Got a bottle!", 0))
    assert (vm2.getBottleCount() == 0)
    assert (vm2.isEmpty() == True)

    # Once a machine is empty, it should not accept money until it is restocked.
    assert (str(vm2) == "Vending Machine:<0 bottles; $1.20 each; $0 paid>")
    assert (vm2.insertMoney(25) == ("Machine is empty", 25))
    assert (vm2.insertMoney(120) == ("Machine is empty", 120))
    assert (vm2.stillOwe() == 120)
    vm2.stockMachine(20)  # Does not return anything
    assert (vm2.getBottleCount() == 20)
    assert (vm2.isEmpty() == False)
    assert (str(vm2) == "Vending Machine:<20 bottles; $1.20 each; $0 paid>")
    assert (vm2.insertMoney(25) == ("Still owe $0.95", 0))
    assert (vm2.stillOwe() == 95)
    vm2.stockMachine(20)
    assert (vm2.getBottleCount() == 40)

    # We should be able to test machines for basic functionality
    vm3 = VendingMachine(50, 100)
    vm4 = VendingMachine(50, 100)
    vm5 = VendingMachine(20, 100)
    vm6 = VendingMachine(50, 200)
    vm7 = "Vending Machine"
    assert (vm3 == vm4)
    assert (vm3 != vm5)
    assert (vm3 != vm6)
    assert (vm3 != vm7)  # should not crash!
    s = set()
    assert (vm3 not in s)
    s.add(vm4)
    assert (vm3 in s)
    s.remove(vm4)
    assert (vm3 not in s)
    assert (vm4.insertMoney(50) == ("Still owe $0.50", 0))
    assert (vm3 != vm4)
    print("Done!")

def getLocalMethods(clss):
    import types
    # This is a helper function for the test function below.
    # It returns a sorted list of the names of the methods
    # defined in a class. It's okay if you don't fully understand it!
    result = []
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if (isinstance(val, types.FunctionType)):
            result.append(var)
    return sorted(result)


def testBirdClasses():
    print("Testing Bird classes...", end="")
    # A basic Bird has a species name, can fly, and can lay eggs
    bird1 = Bird("Parrot")
    assert (type(bird1) == Bird)
    assert (isinstance(bird1, Bird))
    assert (bird1.fly() == "I can fly!")
    assert (bird1.countEggs() == 0)
    assert (str(bird1) == "Parrot has 0 eggs")
    bird1.layEgg()
    assert (bird1.countEggs() == 1)
    assert (str(bird1) == "Parrot has 1 egg")
    bird1.layEgg()
    assert (bird1.countEggs() == 2)
    assert (str(bird1) == "Parrot has 2 eggs")
    assert (getLocalMethods(Bird) == ['__init__', '__repr__', 'countEggs',
                                      'fly', 'layEgg'])

    # A Penguin is a Bird that cannot fly, but can swim
    bird2 = Penguin("Emperor Penguin")
    assert (type(bird2) == Penguin)
    assert (isinstance(bird2, Penguin))
    assert (isinstance(bird2, Bird))
    assert (bird2.fly() == "No flying for me.")
    assert (bird2.swim() == "I can swim!")
    bird2.layEgg()
    assert (bird2.countEggs() == 1)
    assert (str(bird2) == "Emperor Penguin has 1 egg")
    assert (getLocalMethods(Penguin) == ['fly', 'swim'])

    # A MessengerBird is a Bird that can optionally carry a message
    bird3 = MessengerBird("War Pigeon", message="Top-Secret Message!")
    assert (type(bird3) == MessengerBird)
    assert (isinstance(bird3, MessengerBird))
    assert (isinstance(bird3, Bird))
    assert (not isinstance(bird3, Penguin))
    assert (bird3.deliverMessage() == "Top-Secret Message!")
    assert (str(bird3) == "War Pigeon has 0 eggs")
    assert (bird3.fly() == "I can fly!")

    bird4 = MessengerBird("Homing Pigeon")
    assert (bird4.deliverMessage() == "")
    bird4.layEgg()
    assert (bird4.countEggs() == 1)
    assert (getLocalMethods(MessengerBird) == ['__init__', 'deliverMessage'])
    print("Done!")

def testGenerageCharacterString():
    print("Testing generateCharacterString()...", end="")
    assert (generateCharacterString("ko") == "klmno")
    assert (generateCharacterString("") == 0)
    assert (generateCharacterString("22") == "2")
    assert (generateCharacterString("ME") == "MLKJIHGFE")
    print("Passed!")

def testPowersOf3ToN():
    print('Testing powersOf3ToN()...', end='')
    assert(powersOf3ToN(-42) == None)
    assert(powersOf3ToN(0.99) == None)
    assert(powersOf3ToN(1) == [1])
    assert(powersOf3ToN(3) == [1, 3])
    assert(powersOf3ToN(8.9999) == [1, 3])
    assert(powersOf3ToN(9) == [1, 3, 9])
    assert(powersOf3ToN(9.1111) == [1, 3, 9])
    assert(powersOf3ToN(100) == [1, 3, 9, 27, 81])
    print('Done!')

def testPolynomialBasics():
    # we'll use a very simple str format...
    assert(str(Polynomial([1,2,3])) == "Polynomial(coeffs=[1, 2, 3])")
    p1 = Polynomial([2, -3, 5])  # 2x**2 -3x + 5
    assert(p1.degree() == 2)

    # p.coeff(i) returns the coefficient for x**i
    assert(p1.coeff(0) == 5)
    assert(p1.coeff(1) == -3)
    assert(p1.coeff(2) == 2)

    # p.evalAt(x) returns the polynomial evaluated at that value of x
    assert(p1.evalAt(0) == 5)
    assert(p1.evalAt(2) == 7)

def testPolynomialEq():
    assert(Polynomial([1,2,3]) == Polynomial([1,2,3]))
    assert(Polynomial([1,2,3]) != Polynomial([1,2,3,0]))
    assert(Polynomial([1,2,3]) != Polynomial([1,2,0,3]))
    assert(Polynomial([1,2,3]) != Polynomial([1,-2,3]))
    assert(Polynomial([1,2,3]) != 42)
    assert(Polynomial([1,2,3]) != "Wahoo!")
    # A polynomial of degree 0 has to equal the same non-Polynomial numeric!
    assert(Polynomial([42]) == 42)

def testPolynomialConstructor():
    # If the list is empty, treat it the same as [0]
    assert(Polynomial([]) == Polynomial([0]))
    assert(Polynomial([]) != Polynomial([1]))
    # In fact, disregard all leading 0's in a polynomial
    assert(Polynomial([0,0,0,1,2]) == Polynomial([1,2]))
    assert(Polynomial([0,0,0,1,2]).degree() == 1)

    # Require that the constructor be non-destructive
    coeffs = [0,0,0,1,2]
    assert(Polynomial(coeffs) == Polynomial([1,2]))
    assert(coeffs == [0,0,0,1,2])

    # Require that the constructor also accept tuples of coefficients
    coeffs = (0, 0, 0, 1, 2)
    assert(Polynomial(coeffs) == Polynomial([1,2]))

def testPolynomialInSets():
    s = set()
    assert(Polynomial([1,2,3]) not in s)
    s.add(Polynomial([1,2,3]))
    assert(Polynomial([1,2,3]) in s)
    assert(Polynomial([1,2,3]) in s)
    assert(Polynomial([1,2]) not in s)

def testPolynomialMath():
    p1 = Polynomial([2, -3, 5])  # 2x**2 -3x + 5

    # p.scaled(scale) returns a new polynomial with all the
    # coefficients multiplied by the given scale
    p2 = p1.scaled(10) # 20x**2 - 30x + 50
    assert(isinstance(p2, Polynomial))
    assert(p2.evalAt(0) == 50)
    assert(p2.evalAt(2) == 70)

    # p.derivative() will return a new polynomial that is the derivative
    # of the original, using the power rule:
    # More info: https://www.mathsisfun.com/calculus/power-rule.html
    p3 = p1.derivative() # 4x - 3
    assert(type(p3) == Polynomial)
    assert(str(p3) == "Polynomial(coeffs=[4, -3])")
    assert(p3.evalAt(0) == -3)
    assert(p3.evalAt(2) == 5)

    # we can add polynomials together, which will add the coefficients
    # of any terms with the same degree, and return a new polynomial
    p4 = p1.addPolynomial(p3) # (2x**2 -3x + 5) + (4x - 3) == (2x**2 + x + 2)
    assert(type(p4) == Polynomial)
    assert(str(p4) == "Polynomial(coeffs=[2, 1, 2])")
    assert(p1 == Polynomial([2, -3, 5]))
    assert(p4.evalAt(2) == 12)
    assert(p4.evalAt(5) == 57)
    # can't add a string and a polynomial!
    assert(p1.addPolynomial("woo") == None)

    # lastly, we can multiple polynomials together, which will multiply the
    # coefficients of two polynomials and return a new polynomial with the
    # correct coefficients.
    # More info: https://www.mathsisfun.com/algebra/polynomials-multiplying.html

    p1 = Polynomial([1, 3])
    p2 = Polynomial([1, -3])
    p3 = Polynomial([1, 0, -9])
    assert(p1.multiplyPolynomial(p2) == p3) # (x + 3)(x - 3) == (x**2 - 9)
    assert(p1 == Polynomial([1, 3]))

    # (x**2 + 2)(x**4 + 3x**2) == (x**6 + 5x**4 + 6x**2)
    p1 = Polynomial([1,0,2])
    p2 = Polynomial([1,0,3,0,0])
    p3 = Polynomial([1,0,5,0,6,0,0])
    assert(p1.multiplyPolynomial(p2) == p3)

def testPolynomialClass():
    print('Testing Polynomial class...', end='')
    testPolynomialBasics()
    testPolynomialEq()
    testPolynomialConstructor()
    testPolynomialInSets()
    testPolynomialMath()
    print('Passed!')

def testQuadraticClass():
    import math
    print("Testing Quadratic class...", end="")
    # Quadratic should inherit properly from Polynomial
    q1 = Quadratic([3,2,1])  # 3x^2 + 2x + 1
    assert(type(q1) == Quadratic)
    assert(isinstance(q1, Quadratic) and isinstance(q1, Polynomial))
    assert(q1.evalAt(10) == 321)
    assert(str(q1) == "Quadratic(a=3, b=2, c=1)")

    # We use the quadratic formula to find the function's roots.
    # More info: https://www.mathsisfun.com/quadratic-equation-solver.html

    # the discriminant is b**2 - 4ac
    assert(q1.discriminant() == -8)
    # use the discriminant to determine how many real roots (zeroes) exist
    assert(q1.numberOfRealRoots() == 0)
    assert(q1.getRealRoots() == [ ])

    # Once again, with a double root
    q2 = Quadratic([1,-6,9])
    assert(q2.discriminant() == 0)
    assert(q2.numberOfRealRoots() == 1)
    [root] = q2.getRealRoots()
    assert(math.isclose(root, 3))
    assert(str(q2) == "Quadratic(a=1, b=-6, c=9)")

    # And again with two roots
    q3 = Quadratic([1,1,-6])
    assert(q3.discriminant() == 25)
    assert(q3.numberOfRealRoots() == 2)
    [root1, root2] = q3.getRealRoots() # smaller one first
    assert(math.isclose(root1, -3) and math.isclose(root2, 2))

    # Creating a non-quadratic "Quadratic" is an error
    ok = False # the exception turns this to True!
    try: q = Quadratic([1,2,3,4]) # this is cubic, should fail!
    except: ok = True
    assert(ok)
    # one more time, with a line, which is sub-quadratic, so also fails
    ok = False
    try: q = Quadratic([2,3])
    except: ok = True
    assert(ok)

    # And make sure that these methods were defined in the Quadratic class
    # and not in the Polynomial class (we'll just check a couple of them...)
    assert('evalAt' in Polynomial.__dict__)
    assert('evalAt' not in Quadratic.__dict__)
    assert('discriminant' in Quadratic.__dict__)
    assert('discriminant' not in Polynomial.__dict__)
    print("Passed!")

def testEquationClasses():
    testPolynomialClass()
    testQuadraticClass()

def testAll():
    testAlternatingSum()
    testVendingMachineClass()
    testBirdClasses()
    testGenerageCharacterString()
    testPowersOf3ToN()
    testEquationClasses()

def main():
    testAll()

if __name__ == '__main__':
    main()
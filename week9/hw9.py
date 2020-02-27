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

def powersOf3ToN(n):
    return 42

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


def testAll():
    testAlternatingSum()
    testVendingMachineClass()
    testBirdClasses()
    testGenerageCharacterString()

def main():
    testAll()

if __name__ == '__main__':
    main()
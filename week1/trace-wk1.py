import math

# Trace 1
def p(x): print(x, end='   ') # prints and stays on same line
p(3 - 1 + 2 * 6 // 5) # 4
p(3 - 1 + 2 * 6 / 5) # 4.4
p(2**4/10 + 2**4//10) # 2.6
p(max(8/3,math.ceil(8/3))) # 3
print()


# Trace 2
# Note: we provide roundHalfUp and roundHalfEven for you.
# Use these instead of the builtin round function, since that
# function may not behave as you expect.
import decimal
def roundHalfUp(d):
   # Round to nearest with ties going away from zero.
   rounding = decimal.ROUND_HALF_UP
   return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def roundHalfEven(d):
   # Round to nearest with ties going to nearest even integer.
   rounding = decimal.ROUND_HALF_EVEN
   return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def p(x): print(x, end='   ') # prints and stays on same line
p(round(1.5)) # 2
p(roundHalfUp(1.5)) # 2
p(roundHalfEven(1.5)) # 2
print()
p(round(2.5)) # 3
p(roundHalfUp(2.5)) # 3
p(roundHalfEven(2.5)) # 2
print()

# Trace 3
def p(x): print(x, end='   ') # prints and stays on same line
def f(x, y):
  if (x > y):
    if (x > 2*y): p('A')
    else: p('B')
  else:
    p('C')
def g(x, y):
  if (abs(x%10 - y%10) < 2): p('D')
  elif (x%10 > y%10): p('E')
  else:
    if (x//10 == y//10): p('F')
    else: p('G')
f(4,2) # B
f(2,3) # C
f(5,2) # A
print()
g(11,14) # F
g(11,24) # G
g(207,6) # D
g(207,5) # E
print()

# Trace 4
def f(x): return 4*x + 2
def g(x): return f(x//2 + 1)
def h(x):
   print(f(x-3))
   x -= 1
   print(g(x)+x)
   x %= 4
   return g(f(x) % 4) // 2
print(1 + h(6))
# 14, x = 5
# 19, x = 1
# 6

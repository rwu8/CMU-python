#RC1
def rc1(n):
    if ((n < 0) or (n > 99)): return False
    d1 = n%10 # mod returns the ones digit
    d2 = n//10 # integer division returns the tens digit
    m = 10*d1 + d2 # reverse our number
    return ((m < n) and (n < 12)) # answer should be 10


#RC2
def rc2(n):
    if ((n <= 0) or (n > 99)): return False
    if (n//2*2 != n): return False # n must be a multiple of 2
    if (n//5*5 != n): return False # n also multiple of 5 (n must be a multiple of 10)
    return (n//7*7 == n) # also a multiple of 7; 70

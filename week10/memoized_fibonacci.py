# fibResults = dict()
#
# def fib(n):
#     if n in fibResults:
#         return fibResults[n]
#     if (n < 2):
#         return 1
#     else:
#         result = fib(n - 1) + fib(n - 2)
#     fibResults[n] = result
#     return result

def memoized(f):
    import functools
    cachedResults = dict()
    @functools.wraps(f)
    def wrapper(*args):
        if args not in cachedResults:
            cachedResults[args] = f(*args)
        return cachedResults[args]
    return wrapper

@memoized
def fib(n):
    if (n < 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

import time
def testFib(maxN=40):
    for n in range(maxN+1):
        start = time.time()
        fibOfN = fib(n)
        ms = 1000*(time.time() - start)
        print("fib(%2d) = %8d, time =%5dms" % (n, fibOfN, ms))

testFib() # ahhh, much better!
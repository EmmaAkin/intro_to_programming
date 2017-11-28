#
# Fast doubling Fibonacci algorithm
#
# Copyright (c) 2015 Project Nayuki
# All rights reserved. Contact Nayuki for licensing.
# https://www.nayuki.io/page/fast-fibonacci-algorithms
#
import random
import time
st = time.clock()

# (Public) Returns F(n).
def fibonacci(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)

        d = a * a + b * b

        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

def calc_fib(n):
    a,b = 0,1
    if n<=0:return a
    for i in range(1,n):
        a, b = b, a+b
    return b




if __name__ == '__main__':
    m= int(input())
    print(fibonacci(2015)%m)
    print("-- %s secs"%round((time.clock()-st)))
    '''
    while (True):
        a = [random.randint(0,100000)] #for p in range(1)]
        print(a)
        f1 = fibonacci(a[0])
        f2 = calc_fib(a[0])
        if f2 != f1:
            print ("Wrong Answer for :", a)
            print ("f1:%d" %f1)
            print ("f2:%d" %f2)

            break
        else:
            print("Ok:", a)
            print ("f1:%d" %f1)
            print ("f2:%d" %f2)

        '''






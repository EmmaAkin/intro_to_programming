# Uses python3
# (Public) Returns F(n).
import sys
import time, random

st = time.clock()

def fibmod(n,m):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    fibmod = _fib(n)[0]
    return fibmod


# (Private) Returns the tuple (F(n), F(n+1)). Using Matric exponentials
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = (a * (b * 2 - a))%m
        d = (a * a + b * b)%m

        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


if __name__ == '__main__':
    #input = sys.stdin.read()
    #n, m = map(int, input.split())
    while True:
        n= random.randint(100000,10000000000)
        m = random.randint(10,100)
        #m = int(input())


        if round((time.clock()-st)) > 5:
            print ("Take more than 5s for Fibonacci Number index of: {} and modulo: {}".format(n,m))


            break
        else:
            print(fibmod(n,m))
            print("-- %s secs"%round((time.clock()-st)))
# Uses python3
#import time
import random, sys

#st = time.clock()

def pisano(m):
    k = 0
    if m<=1:return 0
    if m==2: return 3

    if m %2==0:
        k=m/2
        pisano = 8*k+4

    else:
        k = (m-1)/2
        pisano = 8*k
    return pisano

def fib(n):
    a,b = 0,1
    if n<=0:return a
    for i in range(1,n):
        a, b = b, a+b
    return b

def fibmod(n,m):
    fibp =n % pisano(m)
    fibmod = fib(int(fibp)) % m
    return int(fibmod)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(fibmod(a, b))

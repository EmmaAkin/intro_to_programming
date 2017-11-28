# Uses python3
#import time
import random, sys

#st = time.clock()

#n  = int(input())
#m = int(input())

def pisano(m):
    for k in range(2, 10**14):
        if m==fib()
    k = 0
    if m<=1:return 0
    if m==2: return 3

    if m %2==0:
        k = (m-1)/2
        pisano = 4*k
    else:
        k=m/2
        pisano = 8*k+4
    print(pisano)
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
    return fibmod

def fibmodslow(n,m):
    return fib(n)%m

if __name__ == '__main__':
    #print(fibmod(n, m))

    while (True):
        a = [random.randint(10,100) for p in range(0,2)]


        f1 = fibmod(2015,5)
        f2 = fibmodslow(2015,5)
        if f2 != f1:
            print ("Wrong Answer for :", a)
            print ("f1:%d" %f1)
            print ("f2:%d" %f2)

            break
        else:
            print("Ok:", a)
            print ("f1:%d" %f1)
            print ("f2:%d" %f2)



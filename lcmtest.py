# Uses python3
#import time
#st = time.clock()
import sys


def gcd(a,b):

    if a==b:
        return a

    while b>0:
        a,b=b,a%b

    #print(a, ",", b)
    return int(a)

def lcm(a,b):
    lcm = (a*b)//(gcd(a,b))
    return int(lcm)

if __name__ == '__main__':
    # input = sys.stdin.read()
    # a, b = map(int, input.split())
    n = int(input())
    m = int(input())

    print (gcd(n,m))
    #print (lcm(226553150,1023473145))
    #print("-- %s secs"%round((time.clock()-st)))
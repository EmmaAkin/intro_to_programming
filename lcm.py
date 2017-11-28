#Uses python3
import time,sys
st = time.clock()


def gcd(a,b):

    if a==b:return a
    while b>0:
        c =a%b
        a = b
        b = c

    return a

def lcm(a,b):
    lcm = a*b/(gcd(a,b))
    return int(lcm)

if __name__ == '__main__':
    #input = sys.stdin.read()
    #a, b = map(int, input.split())
    a = int(input( "Get the first number:"))
    b = int(input( "Get the first number:"))

    print (lcm(a, b))
    print("-- %s secs"%round((time.clock()-st)))
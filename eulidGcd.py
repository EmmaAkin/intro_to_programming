# Uses python3
import sys
c = 0
def gcd(a,b):
    while b>0:
        c = a%b
        a= b
        b = c
        #print(a, ",", b)
    return (int(a))

if __name__ == '__main__':
    #input = sys.stdin.read()
        #a, b = map(int, input.split())
    a = int(input())
    b = int(input())
    print(gcd(a, b))

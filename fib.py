# Uses python3
import random
import time

st = time.clock()



def calc_fib(n):
    a,b = 0,1
    if n<=0:return a
    for i in range(1,n):
        a, b = b, a+b
    return b

def fibMatrix(n):
    ar = Array(n)
    for i in range(2, n):
        fib_num = ar[i-1] +ar[i-2]
            return fib_num





if __name__ == '__main__':
    #n = int(input())
    a = [random.randint(1,10) for p in range(2)]
    b = int(input())

    print(calc_fib(b))
    print("-- %s secs"%round((time.clock()-st)))

'''    for i in range(len(a)):
        print(i,end='  ')
        print(a[i],end = '    ')
        print(calc_fib(a[i]))
'''

    #\print("The Fibonaci of ",n, "is ", "F(",n,") =", calc_fib(n))

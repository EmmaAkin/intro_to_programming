# Uses python3
def calc_fib(n):
    a,b = 0,1
    if n<=0:return a
    for i in range(1,n):
        a, b = b, a+b
        if b>=10:
            b = b -10
    return b

n = int(input())
#print("The Fibonaci of ",n, "is ", "F(",n,") =", calc_fib(n))
print(calc_fib(n))

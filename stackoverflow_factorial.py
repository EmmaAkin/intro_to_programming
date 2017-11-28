def factorial(number):
        return 1 if (number<1) else number * factorial(number-1)

n = int(input().strip())

print("n! = 1", end="")

for num in range(2, n+1):
    print(" x {}". format(num), end="")


print(" = {}".format(factorial(n)))
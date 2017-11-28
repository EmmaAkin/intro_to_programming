
import sys

n = int(input().strip())
text = []

for i in range(0,n):
    text.append(input().strip())

for i in text:
    print("{} {}".format(i[::2],i[1::2]))


# Uses python3
import sys

input = sys.stdin.readline()
#num = input("Get them numbers")
tokens = input.split()
print(int(int(tokens[0])+int(tokens[1])))

import sys

def string_to_int(s):
    try:
            inp = int(s)
            return inp
    except:
            print ("Bad String")

S = input().split()

print(string_to_int(S))
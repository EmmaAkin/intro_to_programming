#!/bin/python3

import sys

def binary_to_decimal(n):
    binary_string = []
    last_largest_consecutives = 0
    present_ones =0

    while (n>0):
        remainder = n%2;

        binary_string.append(remainder)


        n =int(n/2);

    for i in binary_string:

        if i == 1:
            present_ones = present_ones + 1

            if last_largest_consecutives < present_ones:
                last_largest_consecutives = present_ones

        else:
            present_ones = 0



    return last_largest_consecutives
    # binary_string.pop()

    # binary_string.reverse()
    # return "".join(str(i) for i in binary_string)

n = int(input().strip())
print(binary_to_decimal(n))
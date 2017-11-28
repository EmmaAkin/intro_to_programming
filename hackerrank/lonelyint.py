#!/bin/python3

import sys

def lonely_integer(a):
    tmp_a= dict()
    for i in a:
        tmp_a[i] = tmp_a.get(i, 0) + 1
    for key, value in tmp_a.items():
        if value==1:
            return key



n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))

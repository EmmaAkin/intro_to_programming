#!/bin/python3

import sys
#Find the hourglass in an Array

#Example:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0

#Output
#19

def hourglass(arr):

    max_hourglass = 0
    sum_value = 0


    for i in range(1,len(arr[0])-1):
        for j in range(1,len(arr[0])-1):
            #(0,0 0,1 0,2)  (1,0 1,1 1,2) (2,0 2,1 2,2)
            sum_value = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] +  arr[i][j]  +arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            print("This is the position of the calculation {},  {}".format(i,j))
            print("This is the sum: {}".format(sum_value))

            if (j ==1 and i ==1):
                max_hourglass = sum_value
                print("We are here")

            if sum_value > max_hourglass:
                max_hourglass = sum_value
                print("This is the lastest largest number {}".format(max_hourglass))
    return max_hourglass


# arr = [[0, 6, -7, 1, 6, 3], [-8, 2, 8, 3, -2, 7], [-3, 3, -6, -3, 0, -6], [5, 0, 5, -1, -5, 2], [6, 2, 8, 1, 3, 0], [8, 5, 0, 4, -7, 4]]
arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

print(hourglass(arr))
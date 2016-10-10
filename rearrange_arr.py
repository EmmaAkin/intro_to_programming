
def min_arr(a):
    min_num = -1

    for i in range(0, len(a)):
        if min_num==-1 or (a[i]< a[min_num]):
           min_num = i
    return a[min_num]

def max_arr(a):
    max_num = -1

    for i in range(0, len(a)):
        if max_num==-1 or (a[i]> a[max_num]):
           max_num = i
    return a[max_num]

    # for j in range(0, len(a)):
    #     if (j != maxindex1) and (maxindex2==-1 or (a[j]< a[maxindex2])):
    #         print (j)
    #         maxindex2 = j
def sorting(arr, choice ="asc"):
    sorted_array = []
    if choice == "asc":
        for i in range(len(arr)):
            min_num = min_arr(arr)
            sorted_array.append(min_num)
            arr.remove(min_num)
    else:
        for i in range(len(arr)):
            max_num = max_arr(arr)
            sorted_array.append(max_num)
            arr.remove(max_num)

    return sorted_array


def sort_re(arr):
    re_arr = []
    # find the sorted array
    sorted_arr = sorting(arr)
    # Find the mid point of the array
    mid = int((len(sorted_arr)+1)/2)

    # Sort this in the ascending order
    asc = sorted_arr[:int(mid)]

    desc = sorting(sorted_arr[mid:],choice="desc")

    re_arr = asc + desc

    return re_arr

def sec_sec_to_last(arr):
    # return the second and second to the last elment of a sorted array
    sorted_arr = [min_arr(arr), max_arr(arr)]
    return sorted_arr

def snake_case(arr):
    snake_string = ""
    for c in arr:
        if ord(c) >= 65 and ord(c)<=90:
            snake_string = snake_string + "_" + c.lower()
        else:
            snake_string = snake_string + c
    return snake_string

print(sec_sec_to_last([1,3,5,4,5,6,76]))

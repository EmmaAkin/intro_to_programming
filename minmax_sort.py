def minmax_sort(a):
    sorted_arr = []
    while len(a)>1:
        min_el = min(a)
        sorted_arr.append(min_el)
        a.remove(min_el)

        max_el = max(a)
        sorted_arr.append(max_el)
        a.remove(max_el)

    return sorted_arr

a = [1,5,3,2,8,9,4,45]
print(minmax_sort(a))
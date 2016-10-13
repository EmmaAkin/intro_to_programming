def subsets(my_set):
    result = [[]]
    for x in my_set:
        result = result + [y + [x] for y in result]
        print(result)
    return result


a = [1,2,3]
print(subsets(a))
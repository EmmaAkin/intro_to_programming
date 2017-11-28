import random, time

st = time.clock()
def merge_sort(a):
    sorted_array =[]
    print("Splitting the list ",a)

    if len(a)>1:
        lefthalf =a[:(len(a)//2)]
        righthalf = a[(len(a)//2):]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i, j, k = 0, 0, 0

        while i < len(lefthalf) and j < len(righthalf) :

            if lefthalf[i] < righthalf[j]:
                a[k] = lefthalf[i]
                i +=1
            else:
                a[k] = righthalf[j]
                j +=1
            k += 1

        while i < len(lefthalf):
            a[k] = lefthalf[i]
            i +=1
            k +=1

        while j < len(righthalf):
            a[k] = righthalf[j]
            j +=1
            k +=1

        print("Merging the array: ",a)
    return a
if __name__ == '__main__':
    a = [random.randint(0,1000) for p in range(0,10000)]

    print(merge_sort(a))
    print("-- %s secs"%round((time.clock()-st)))
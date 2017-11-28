# Uses python3
import random, sys

def maxpairwisefast(a):

    maxindex1 = -1
    maxindex2 = -1
    result = 0

    for i in range(0, len(a)):
        if maxindex1==-1 or (a[i]> a[maxindex1]):
            print (i)
            maxindex1 = i

    for j in range(0, len(a)):
        if (j != maxindex1) and (maxindex2==-1 or (a[j]> a[maxindex2])):
            print (j)
            maxindex2 = j

    result = a[maxindex1]*a[maxindex2]
    return result

def maxpairwisefastest(a):
    max_index1, max_index2 = -1, -1

    for i in range(len(a)):
        print(a[i])
        if max_index1 == -1 or max_index1 < a[i]:
            max_index2 = max_index1
            max_index1 = a[i]
        elif max_index2 < a[i]:
            max_index2 = a[i]
    return max_index1 * max_index2

def maxpairwise(a):
    result = 0

    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
    return result

if __name__ == '__main__':
    #print ([1,2,3,45])
    #print(maxpairwisefast([1,2,3,45]))

    while (True):
        a = [random.randint(1,10) for p in range(0,10)]

        f1 = maxpairwise(a)
        f2 = maxpairwisefastest(a)
        if f2 != f1:
            print ("Wrong Answer for :", a)
            print ("f1:%d" %f1)
            print ("f2:%d" %f2)

            break
        else:
            print("Ok:", a)
            print ("f1:%d" %f1)
            print ("f2:%d" %f2)

import random, time
st = time.clock()

def bubble_sort(a):
 for i in range(len(a)-1,0,-1):
   for j in range(i):
    print("This is i ", i)
    print("This is j ", j)
    if a[j]>a[j+1]:
        print(a)
        temp = a[j]
        a[j] = a[j+1]
        a[j+1] = temp
        print(a)

 return a


if __name__ == '__main__':
    a = [random.randint(0,1000) for p in range(0,10000)]


    print(bubble_sort(a))

    print("-- %s secs"%round((time.clock()-st)))
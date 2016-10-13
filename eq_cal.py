

def gcd(a,b):
    if a==b:
        return a
    while b>0:
        a,b=b,a%b
    return int(a)

def cal_simultanous_eq(unknow, arr):
    result = []
    if unknow != len(arr):
        return "Wrong Entry, the Unknow must match the number of array given"

    #Using the elimination method to find the result of the simultanous equation
    # x = (c1-c2)/(a1b1-a2b1) where a, b,c are the coefficient in the equation
    if unknow ==1:
        x = (0-arr[1])/arr[0]

        return (x)

    if unknow == 2:
        a1 = a[0][0]
        b1 = a[0][1]
        c1 = a[0][2]
        a2 = a[1][0]
        b2 = a[1][1]
        c2 = a[1][2]
        #Reduce the fraction
        x = (c1-c2)/(a1*b1-a2*b1)

        y =(c1-c2)/(a2*b1-a1*b2)




        return (x,y)


a = [(2,3,4),(4,5,6)]
unknow = 2
print(cal_simultanous_eq(unknow, a))

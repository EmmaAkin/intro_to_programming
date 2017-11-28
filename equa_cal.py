class Fraction:
    def __init__(self,top, bottom):
            self.num = top//gcd(top,bottom)
            self.den= bottom//gcd(top,bottom)
    def __add__(self, other_fraction):
        #print("Not set yet")
        new_num = self.num*other_fraction.den+ self.den*other_fraction.num
        new_den = self.den * other_fraction.den
        # Factor the fraction to reduce the fraction

        red_num = new_num//gcd(new_num,new_den)
        red_den = new_den//gcd(new_num,new_den)

        return str(red_num)+"/"+str(red_den)

    def __str__(self):
        return str(self.num)+ "/"+str(self.den)

    def show(self):
        return (self.num, "/", self.den)

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
        x = Fraction((0-arr[1]),arr[0])

        return (x)

    if unknow == 2:
        a1 = a[0][0]
        b1 = a[0][1]
        c1 = a[0][2]
        a2 = a[1][0]
        b2 = a[1][1]
        c2 = a[1][2]
        #Reduce the fraction
        x = Fraction((c1-c2),(a1*b1-a2*b1))

        y = Fraction((c1-c2),(a2*b1-a1*b2))

        num = x
        den = y


        return (num,den)


a = [(2,3,4),(4,5,6)]
unknow = 2
print(cal_simultanous_eq(unknow, a))

class Duck():
    def __init__(self, **kwargs):
        self.variables = kwargs

    def set(self, k, v):
        self.variables[k]=v

    def get(self,k):
        return self.variables.get(k,None)

def main():
    yaw = Duck(color = "Blackl", legs = 2)
    # yaw.set(feet, 2)
    print(yaw.get("color"))
    yaw.set("feet", "2")
    print(yaw.get("feet"))
    print(yaw.get("legs"))



if __name__ == '__main__':
    main()
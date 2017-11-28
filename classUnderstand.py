#Understanding class
class PartyAnimal(object):
    """docstring for ClassName"""
    name=""
    x = 0
    def __init__(self, name):
        self.name = name
        print (self.name, "Constructed ")
    def party(self):
        self.x= self.x+1
        print (self.name, "Party count ", self.x)

if __name__ == '__main__':
    s = PartyAnimal("Sally")
    s.party()

    p = PartyAnimal("Paul")
    p.party()
    s.party()
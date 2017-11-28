class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


# s = Stack()

# print(s.is_empty())
# s.push("dog")
# s.push(3)
# s.push("there it is")

# s.pop()

# print(s.size())


# m = Stack()
# m.push('x')
# m.push('y')
# m.pop()
# m.push('z')
# print("This is for the second element {}" .format(m.peek()))
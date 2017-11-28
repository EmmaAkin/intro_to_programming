class Stack():
    """docstring for ClassName"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]


def Solution(S):
    k = 0
    stack_op = Stack()

    for i in S:
        if i == "(":
            stack_op.push(i)

        elif not stack_op.isEmpty() and i == ")":
            stack_op.pop()
            k = +1
    return k*2
print(Solution("(())"))






# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

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

def solution(S):
    # write your code in Python 2.
    k = 0
    op_stack = Stack()
    for i in S:
        if i =="(":
            op_stack.push(i)
        elif not op_stack.is_empty() and i == ")":
            op_stack.pop()

            k+=1
    return k*2
print(solution(")(((()0*(jkljfjkfdf(99999((()))))))("))
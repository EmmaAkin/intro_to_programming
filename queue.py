class Queue:
    # The construct of the Queue class with the property of FIFO
    def __init__(self):
        self.items = []

    #Return True if the items in the queue is empty
    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self, item):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def display(self):
        return self.items

# t = int(input("Enter the number of items you want to insert: "))
# q = Queue()

# items = list(map(str, input().split()))


# for item in items:

#     q.enqueue(item)
#     print("{}".format(q.display()))

# for item in items:
#     print("{}".format(q.display()))
#     q.dequeue(item)




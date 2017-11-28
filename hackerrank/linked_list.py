class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Solution:
    #Display method takes data and returns data seperated output
    def display(self,head):
        current = head

        while current:
            print(current.data,end=' ')
            current = current.next
        print(head)


    def insert(self,head,data):
    #Complete this method

            new_node = Node(data)
            print("This is the new data {}".format(new_node.data))
            new_node.next = head








mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head =mylistylist.insert(head,data)
    print(head)
mylist.display(head);
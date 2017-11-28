import sys
from datetime import datetime


number_of_input = int(input().strip())
phonebook = []
query = []

for inputs in range(0,number_of_input):
    phonebook.append(tuple(map(str,  input().strip().split(" "))))

for inputs in range(0,number_of_input):
    query.append(input().strip())


phonebook = dict(phonebook)

# print(phonebook.items())
start=datetime.now()
for name in query:
    if  name in phonebook.keys():
        print("{} = {}".format(name, phonebook[name]))
    else:
        print("Not found")

print (datetime.now() - start)


# import sys

# n = int(input().strip())
# phonebook =[]
# query =[]

# for i in range(0,n):
#     phonebook.append(tuple(map(str, input().strip().split(" "))))

# for i in range(0,n):
#     query.append(str(input().strip()))

# i =0
# for name in query:

#     if name in phonebook[i]:
#             print("Found {}".format(name))
#     else:
#         print("Not Found")
#     i +=1
scores = list( map(int, input().split()) )

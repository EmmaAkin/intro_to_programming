# Function that sort the list
def sort_list(a):
 for my_number in range(len(a)-1,0,-1):
   for i in range(my_number):
     if a[i][0]>a[i+1][0]:
         temp = a[i]
         a[i] = a[i+1]
         a[i+1] = temp
 return a

# Find the freetime between people
def condensed_meeting_time(arr):
    free_time = []
    arr = sort_list(arr)
#Find the different between the last previous elment in the tuple and the first elment in the present tuple
    if arr[0][0]!=0:
        free_time.append((0,arr[0][0]))

    for i in range(0,len(arr)-1,1):
        # If less present_last_elment <  next_first_element find the differences

        if arr[i][1]>arr[i+1][1]:
            lst_time = arr[i][1]
        elif arr[i][1]>arr[i+1][0]:
            lst_time = arr[i+1][1]
        else:
            lst_time = arr[]

        if arr[i][1] < arr[i+1][0]:
            free_time.append((a[i][1],a[i+1][0]))

    if arr[-1][-1] > 0 or arr[-1][-1] < 24:
        free_time.append((arr[-1][-1],0))

    return free_time



a = [(7,9),(10,11),(13,17)]
print(a)
print(condensed_meeting_time(a))
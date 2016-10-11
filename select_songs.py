
def sort_list(a):
 for my_number in range(len(a)-1,0,-1):
   for i in range(my_number):
     if a[i][1]>a[i+1][1]:
         temp = a[i]
         a[i] = a[i+1]
         a[i+1] = temp
 return a

def select_song(songs, time):
    songs = sort_list(songs)
    selected_song =[]
    sum_time = 0
    for song in songs:
        sum_time = sum_time + song[1]
        if sum_time <= time:
            selected_song.append(song)
        else:
           break
    return selected_song


# def sorted_list(arr):
#     sorted_arr = []
#     min_time = -1

#     for i in range(0, len(a)):
#         if min_num==-1 or (a[i]< a[min_num]):
#            min_num = i
#     return a[min_num]

#     return sorted_arr



print(select_song([("time", 3),("time", 14),("time", 5)],900))

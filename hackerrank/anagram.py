# What I learn from here is that you need to know exactly what your algo is doing.
# First I used the counter such that if the key does not exists, the counter increases
# LIne 12 looks like this counter +=1 and while line 17 is counter +=1
# But this bring an semantic error that when the letter is not in the second dictionary, the counter increases by
# 1 rather than increasing by the value of the character. So a = {"a":2, "b":4}, b= {"c":2, "b":4}
# The counter read 1+1 rather than 2+2
def equality_hash(a,b):
    counter = 0
    print(a)
    print(b)
    for key, value in a.items():
        if key in b:
            counter = counter + abs(b[key]-a[key])
        else:
            counter = counter + value

    for key, value in b.items():
        if key in a: continue
        else:
            counter = counter + value

    return counter

def number_needed(a, b):
    tmp_a = dict()
    tmp_b = dict()
    for i in a:
        tmp_a[i] = tmp_a.get(i, 0) + 1
    for i in b:
        tmp_b[i] = tmp_b.get(i, 0) + 1


    if len(tmp_a)==len(tmp_b):
        return equality_hash(tmp_a, tmp_b)
    elif len(tmp_a)>len(tmp_b):
        return equality_hash(tmp_a, tmp_b)
    else:
        return equality_hash(tmp_b, tmp_a)





# a = input().strip()
# b = input().strip()

a = "bugexikjevtubidpulaelsbcqlupwetzyzdvjphn".strip()
b = "lajoipfecfinxjspxmevqxuqyalhrsxcvgsdxxkacspbchrbvvwnvsdtsrdk".strip()



# print(len(a))
# print(len(ab))

print(number_needed(a, b))

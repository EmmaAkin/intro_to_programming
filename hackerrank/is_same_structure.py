def is_same_structure(a,b):
    horizontal = 0
    depth = 0
    for i in a:
        if type(i) is list:
            horizontal +=1

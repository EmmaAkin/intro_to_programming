def knightsmoves(x, y):
    delta = x-y

    if(y>delta):
        return 2 * floor((y - delta) / 3) + delta
    else:
        return delta - 2 * floor((delta - y) / 4)

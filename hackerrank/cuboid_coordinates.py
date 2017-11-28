def generate_2d(x, y):
    coord_2d = list()
    for x in range(x+1):
        for y in range(y+1):
            coord_2d.append([x,y])

    return coord_2d

def generate_3d(x, y, z):
    coord_3d = list()
    coord_2d = generate_2d(x,y)

    print(coord_2d)
    for x in coord_2d:
        for z in range(z+1):
            x.append(z)
            coord_3d.append(x)

    return coord_3d

n = int(input())
x, y, z = map(int, input().split())

print(generate_3d(x,y, z))


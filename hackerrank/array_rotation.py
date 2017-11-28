def array_left_rotation(a, n, k):
    tmp = [0]*n
    for i in range(n):
        tmp[(i-k)]= a[i]
    return tmp



n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

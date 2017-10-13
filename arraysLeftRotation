def array_left_rotation(a, n, k):
    outputArray = []
    for i in range(n):
        outputArray.append(0)
    for i in range(n):
        shift = (i - k) % n
        outputArray[shift] = a[i]
    return outputArray

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
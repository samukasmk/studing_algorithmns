array = [1, -5, 200, 9, 56, -34]

n = len(array)

for leftmost in range(n - 1):
    minor = leftmost

    for i in range(leftmost, n):
        if array[i] < array[minor]:
            minor = i

    if minor != leftmost:
        array[leftmost], array[minor] = array[minor], array[leftmost]

print(array)
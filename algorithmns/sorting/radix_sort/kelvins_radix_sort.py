import random


def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Do counting sort for every digit, starting from the least significant digit
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def main():
    print("Fixed Testing Array")
    arr = [170, 2, 45, 75, 75, 90, 802, 24, 2, 66]
    print("Unsorted array:", arr)
    radix_sort(arr)
    print("Sorted array:", arr)

    print("Random Testing Array")
    arr = []
    for i in range(0, 10):
        arr.append(random.randint(0, 20))
    print("Unsorted array:", arr)
    radix_sort(arr)
    print("Sorted array:", arr)


# if __name__ == "__main__":
#     main()

if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    radix_sort(numbers)

    # check if the original list was sorted
    if numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]:
        print(f'Sorted list: {numbers}')
    else:
        print(f"Final is not sorted: {numbers}")
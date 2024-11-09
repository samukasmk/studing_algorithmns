# Reference: https://www.geeksforgeeks.org/bubble-sort-algorithm/

# Optimized Python program for implementation of Bubble Sort
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if (swapped == False):
            break


# # Driver code to test above
# if __name__ == "__main__":
#     arr = [64, 34, 25, 12, 22, 11, 90]
#
#     bubbleSort(arr)
#
#     print("Sorted array:")
#     for i in range(len(arr)):
#         print("%d" % arr[i], end=" ")

if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    bubbleSort(numbers)
    print(f'Final list: {numbers}')

    # check if the original list was sorted
    assert numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100], f"List is not sorted: {numbers}"

    # print the sorted list
    print(f'Sorted list: {numbers}')
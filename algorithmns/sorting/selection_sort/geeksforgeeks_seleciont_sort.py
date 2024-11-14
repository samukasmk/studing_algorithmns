# Reference: https://www.geeksforgeeks.org/selection-sort-algorithm-2/

# Python program for implementation of Selection
# Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):

        # Assume the current position holds
        # the minimum element
        min_idx = i

        # Iterate through the unsorted portion
        # to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                # Update min_idx if a smaller element is found
                min_idx = j

        # Move minimum element to its
        # correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()


# if __name__ == "__main__":
#     arr = [64, 25, 12, 22, 11]
#
#     print("Original array: ", end="")
#     print_array(arr)
#
#     selection_sort(arr)
#
#     print("Sorted array: ", end="")
#     print_array(arr)


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    selection_sort(numbers)

    # check if the original list was sorted
    if numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]:
        print(f'Sorted list: {numbers}')
    else:
        print(f"Final is not sorted: {numbers}")
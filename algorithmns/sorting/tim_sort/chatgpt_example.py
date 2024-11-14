def insertion_sort(arr, left, right):
    """
    Perform insertion sort on the given array within the specified range.

    Args:
        arr: The array to be sorted.
        left: The left index of the range.
        right: The right index of the range.
    """
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, left, mid, right):
    """
    Merge two sorted subarrays within the array.

    Args:
        arr: The array containing the subarrays to be merged.
        left: The left index of the first subarray.
        mid: The right index of the first subarray.
        right: The right index of the second subarray.
    """
    len1 = mid - left + 1
    len2 = right - mid

    # Create temporary arrays for the two subarrays
    left_arr = [0] * len1
    right_arr = [0] * len2

    # Copy data to the temporary arrays
    for i in range(len1):
        left_arr[i] = arr[left + i]
    for i in range(len2):
        right_arr[i] = arr[mid + 1 + i]

    # Merge the temporary arrays back into arr
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    while i < len1 and j < len2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # Copy the remaining elements of left_arr, if any
    while i < len1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of right_arr, if any
    while j < len2:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def timsort(arr):
    """
    Perform Timsort on the given array.

    Args:
        arr: The array to be sorted.
    """
    min_run = 32  # Minimum size of a run

    n = len(arr)
    # Perform insertion sort on small runs
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    # Merge runs in a bottom-up manner
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = min(start + size - 1, n - 1)
            end = min(start + size * 2 - 1, n - 1)
            merge(arr, start, mid, end)
        size *= 2


# # Example usage:
# arr = [5, 2, 8, 1, 3]
# timsort(arr)
# print(arr)  # Output: [1, 2, 3, 5,

if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    timsort(numbers)

    # check if the original list was sorted
    if numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]:
        print(f'Sorted list: {numbers}')
    else:
        print(f"Final is not sorted: {numbers}")
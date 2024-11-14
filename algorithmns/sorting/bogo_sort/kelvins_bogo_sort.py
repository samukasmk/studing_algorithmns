""" Implementation of the bogosort algorithm in Python. """

import random


def is_sorted(arr):
    """Checks if an array is sorted.

    Args:
        arr (list): The array to check.

    Returns:
        bool: True if the array is sorted, False otherwise.
    """
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


# Time: O(n * n!)
# Space: O(1)
def bogosort(arr):
    """Sorts an array using the bogosort algorithm.

    Args:
        arr (list): The array to sort.

    Returns:
        None: The array is sorted in place.
    """
    while not is_sorted(arr):
        random.shuffle(arr)


# if __name__ == "__main__":
#     # Example usage
#     unsorted_list = [3, 1, 2, 5, 4]
#     print("Unsorted list:", unsorted_list)
#
#     bogosort(unsorted_list)
#     print("Sorted list:", unsorted_list)


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    bogosort(numbers)

    # check if the original list was sorted
    if numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]:
        print(f'Sorted list: {numbers}')
    else:
        print(f"Final is not sorted: {numbers}")

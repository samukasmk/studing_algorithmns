"""
Bubble Sort Algorithm

Complexity:
- Time: O(n^2)
- Space: O(1)
"""


def bubble_sort(array: list[int]) -> list[int]:
    n = len(array)

    for position in range(n - 1):

        for current_index in range(n - 1 - position):
            next_index = current_index + 1

            # swap items if is greater (for ascending order) [change to less (for descending order)]
            if array[current_index] > array[next_index]:
                array[current_index], array[next_index] = array[next_index], array[current_index]

    return array


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    bubble_sort(numbers)

    # check if the original list was sorted
    assert numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]

    # print the sorted list
    print(f'Sorted list: {numbers}')

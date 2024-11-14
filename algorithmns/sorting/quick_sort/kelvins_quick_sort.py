""" Quick Sort in Python """
from algorithmns.sorting.selection_sort.hallisonpaz_selection_sort import quicksort


def swap(a_list, pos1, pos2):
    """Swaps the position of two items in a list"""
    temp = a_list[pos1]
    a_list[pos1] = a_list[pos2]
    a_list[pos2] = temp


def partition(a_list, start, end):
    """Splits a list"""
    pivot = a_list[start]
    while True:
        while a_list[start] < pivot:
            start = start + 1

        while a_list[end] > pivot:
            end = end - 1

        if start >= end:
            return end

        swap(a_list, start, end)

        start = start + 1
        end = end - 1


def quick_sort(a_list, start, end):
    """Quick sort algorithm"""
    if start < end:
        part = partition(a_list, start, end)
        quick_sort(a_list, start, part)
        quick_sort(a_list, part + 1, end)


# if __name__ == "__main__":
#     a = [9, 8, 5, 7, 6, 2, 4, 3, 1]
#     print(a)
#     quick_sort(a, 0, len(a) - 1)
#     print(a)


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    quicksort(numbers)

    # check if the original list was sorted
    if numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]:
        print(f'Sorted list: {numbers}')
    else:
        print(f"Final is not sorted: {numbers}")
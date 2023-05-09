"""
Binary search:
    It's a search in an ordered array that takes well less time to find a element compared to a linear search
Developed by:
    Samuel Sampaio [20230406] @samukasmk
Goal:
    Do not use the use of recursion for objects with billionaire elements
    avoiding python's limitation with the maximum number of recursions (around 999)
Big O complexity analyses:
    O(log n)
For billionaire case:
    for 100000 elements it takes 20 steps to search the desirable element
Calculation:
    divide to base 2 until rest 0
Sample:
    1000000 // 2 // 2 // 2 // 2 // 2 // 2 // 2 // 2 // 2 // 2 // 2 // 2 // 2 // 2 // 2 // 2 // 2 // 2 // 2 // 2
Smart calculation:
    >>> from math import log
    >>> log(1000000, 2)
    19.931568569324174
"""


def binary_search(array, element_to_search):
    while len(array) > 0:
        middle_index = len(array) // 2
        middle_element = array[middle_index]
        if element_to_search == middle_element:
            return True
        elif element_to_search > middle_element:
            array = array[middle_index + 1:]
        elif element_to_search < middle_element:
            array = array[:middle_index]
    return False

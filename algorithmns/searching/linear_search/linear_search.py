"""
Solution: linear O(n)
"""


def linear_search(array, element_to_search):
    for i in range(len(array)):
        if array[i] == element_to_search:
            return True
    return False

if __name__ == '__main__':
    if linear_search([0, 4, 3, 5, 2, 6, 1, 7, 5], 6):
        print('Element 6: was found')
    else:
        print('Element 6: was NOT found')
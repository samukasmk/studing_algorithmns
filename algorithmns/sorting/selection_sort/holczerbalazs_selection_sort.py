
def selection_sort(nums):

    # we make N-1 iterations
    # N-1 x O(N) = O(NxN)
    for i in range(len(nums)-1):

        # linear search and the index stores the index
        # of the min item
        index = i

        # THIS IS THE LINEAR SEARCH - O(N)
        for j in range(i, len(nums)):
            if nums[index] > nums[j]:
                index = j

        # we have to swap the min item with the left-most item
        # we do not swap the item with itself
        if index != i:
            nums[index], nums[i] = nums[i], nums[index]


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    selection_sort(numbers)

    # check if the original list was sorted
    assert numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]

    # print the sorted list
    print(f'Sorted list: {numbers}')
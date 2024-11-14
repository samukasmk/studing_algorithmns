
def shell_sort(nums):

    gap = len(nums) // 2

    # this is the shell sort
    while gap > 0:

        # this is the same as insertion sort BUT here we have to consider
        # items that are as far away from each other as the value of the 'gap'
        for i in range(gap, len(nums)):

            j = i

            while j >= gap and nums[j - gap] > nums[j]:
                nums[j], nums[j - gap] = nums[j - gap], nums[j]
                j = j - gap

        gap = gap // 2


# if __name__ == '__main__':
#
#     x = [10, -4, 0, 3, 2, 1, 100, -8]
#     shell_sort(x)
#     print(x)

if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    shell_sort(numbers)

    # check if the original list was sorted
    if numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]:
        print(f'Sorted list: {numbers}')
    else:
        print(f"Final is not sorted: {numbers}")
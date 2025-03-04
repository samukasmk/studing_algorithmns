
class BubbleSort:

    def __init__(self, nums):
        self.nums = nums

    def sort(self):

        for i in range(len(self.nums)-1):
            for j in range(len(self.nums)-i-1):
                if self.nums[j] < self.nums[j+1]:
                    self.swap(j, j+1)

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]


# if __name__ == '__main__':
#
#     n = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
#     bubble_sort = BubbleSort(n)
#     bubble_sort.sort()
#     print(bubble_sort.nums)


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    algorithm = BubbleSort(numbers)
    algorithm.sort()

    # check if the original list was sorted
    if numbers == [100, 56, 10, 9, 2, 1, 0, -1, -5, -34]:
        print(f'Sorted list: {numbers}')
    else:
        print(f"Final is not sorted: {numbers}")
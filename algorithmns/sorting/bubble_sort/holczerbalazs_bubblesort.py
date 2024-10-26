class BubbleSort:

    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        for i in range(len(self.nums) - 1):
            for j in range(len(self.nums) - i - 1):
                if self.nums[j] > self.nums[j + 1]:
                    self.swap(j, j + 1)

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    bubble_sort = BubbleSort(numbers)
    bubble_sort.sort()

    # check if the original list was sorted
    assert bubble_sort.nums == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]

    # print the sorted list
    print(f'Sorted list: {numbers}')

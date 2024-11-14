
class CountingSort:

    def __init__(self, data):
        self.data = data
        # k = max - min + 1
        self.count_array = [0 for _ in range(max(data)-min(data)+1)]

    def sort(self):

        # first we have to consider all the items in data in O(N) running time
        # indexes start with 0 + we should handle negative values as well
        for i in range(len(self.data)):
            self.count_array[self.data[i]-min(self.data)] += 1

        # we have to consider the counting array in O(k)
        z = 0
        for i in range(min(self.data), max(self.data)+1):
            while self.count_array[i-min(self.data)] > 0:
                self.data[z] = i
                z += 1
                self.count_array[i - min(self.data)] -= 1


# if __name__ == '__main__':
#
#     n = [4, 6, -3, 0, 10, 14, 22, 5]
#     counting_sort = CountingSort(n)
#     counting_sort.sort()
#     print(counting_sort.data)


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    algorithm = CountingSort(numbers)
    algorithm.sort()

    # check if the original list was sorted
    if algorithm.data == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]:
        print(f'Sorted list: {algorithm.data}')
    else:
        print(f"Final is not sorted: {algorithm.data}")

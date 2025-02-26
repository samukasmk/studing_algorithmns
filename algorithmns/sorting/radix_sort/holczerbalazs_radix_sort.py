import random

ITEMS_IN_BUCKET = 10


class RadixSort:

    def __init__(self, data):
        self.data = data
        self.operations = 0

    def get_digits(self):
        self.operations += len(self.data)  # max function is O(n) complexity
        return len(str(max(self.data)))

    def sort(self):
        for digit in range(self.get_digits()):
            self.counting_sort(digit)

    def counting_sort(self, d):

        count_array = [[] for _ in range(ITEMS_IN_BUCKET)]

        # store the count of each element in count array O(N)
        for num in self.data:
            # calculate the index of the given bucket
            index = (num // (10 ** d)) % 10
            count_array[index].append(num)
            self.operations += 1

        # we have to consider all the items in the count array (list)
        z = 0
        for i in range(len(count_array)):
            while len(count_array[i]) > 0:
                # it takes O(N) linear running time complexity - dictionary O(1)
                self.data[z] = count_array[i].pop(0)
                z += 1
                self.operations += 1


# if __name__ == '__main__':
#
#     n = [5, 3, 10, 12, 9, 8, 20, 100, 325, 1023]
#     random.shuffle(n)
#     print(n)
#     radix_sort = RadixSort(n)
#     radix_sort.sort()
#     print(radix_sort.data)

if __name__ == '__main__':
    # define a list of numbers
    numbers = [5, 3, 10, 12, 9, 8, 20, 100, 325, 1023]
    print(f'Initial list: {numbers}')

    # sort elements
    algorithm = RadixSort(numbers)
    algorithm.sort()

    # check if the original list was sorted
    if algorithm.data == [3, 5, 8, 9, 10, 12, 20, 100, 325, 1023]:
        print(f'Sorted list: {algorithm.data}')
    else:
        print(f"Final is not sorted: {algorithm.data}")

    print('\nConsiderations:')
    print('-> O(n) complexity is:', len(algorithm.data), 'operations.')
    print('-> O(n)² quadratic complexity is:', len(algorithm.data) ** 2, 'operations.')
    print('-> Most of sorting algorithms are O(n)² quadratic complexity...')
    print('-> This algorithm took:', algorithm.operations, 'operations. In other words - O(nk) complexity!')
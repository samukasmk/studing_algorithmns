def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[0]
    # sub-array of all the elements less than the pivot
    less = [i for i in array[1:] if i <= pivot]
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

# print(quicksort([10, 5, 2, 3]))


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
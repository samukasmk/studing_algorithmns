import time
import random

from radix_sort.holczerbalazs_radix_sort import RadixSort
from quick_sort.holczerbalazs_quick_sort import QuickSort
from shell_sort.holczerbalazs_shell_sort import shell_sort
from selection_sort.holczerbalazs_selection_sort import selection_sort
from insertion_sort.holczerbalazs_insertion_sort import insertion_sort
from bubble_sort.holczerbalazs_bubble_sort import BubbleSort
from counting_sort.holczerbalazs_counting_sort import CountingSort
# from bogo_sort.holczerbalazs_bogo_sort import BogoSort

# preparing data arrays
sorted_array = [n for n in range(10001)]
reversed_array = list(sorted_array)
reversed_array.reverse()
shuffled_array = list(sorted_array)
random.shuffle(shuffled_array)

initial_data = ', '.join([str(i) for i in sorted_array[0:5] + ['<rest of 10000 elements>'] + sorted_array[9995:10000]])
print(f'[{initial_data}]')

# Radix sort
array = list(shuffled_array)
assert array != sorted_array
radix = RadixSort(array)
t = time.time()
radix.sort()
print(f'Radix sort\ttime taken: {str(time.time() - t)}')
assert array == sorted_array

# Quick sort
array = list(shuffled_array)
assert array != sorted_array
quick = QuickSort(array)
t = time.time()
quick.sort()
print(f'Quick sort\ttime taken: {str(time.time() - t)}')
assert array == sorted_array

# Shell sort
array = list(shuffled_array)
assert array != sorted_array
t = time.time()
shell_sort(array)
print(f'Shell sort\ttime taken: {str(time.time() - t)}')
assert array == sorted_array

# Selection sort
array = list(shuffled_array)
assert array != sorted_array
t = time.time()
selection_sort(array)
print(f'Selection sort\ttime taken: {str(time.time() - t)}')
assert array == sorted_array

# Insertion sort
array = list(shuffled_array)
assert array != reversed_array
t = time.time()
insertion_sort(array)
print(f'Insertion sort\ttime taken: {str(time.time() - t)}')
assert array == reversed_array

# Bubble sort
array = list(shuffled_array)
assert array != reversed_array
bubble = BubbleSort(array)
t = time.time()
bubble.sort()
print(f'Bubble sort\ttime taken: {str(time.time() - t)}')
assert array == reversed_array

# Counting sort
array = list(shuffled_array)
assert array != sorted_array
counting = CountingSort(array)
t = time.time()
counting.sort()
print(f'Counting sort\ttime taken: {str(time.time() - t)}')
assert array == sorted_array

# # Bogo sort
# array = list(shuffled_array)
# assert array != sorted_array
# bogo = BogoSort(array)
# t = time.time()
# bogo.sort()
# print(f'Bogo sort\ttime taken: {str(time.time() - t)}')
# assert array == sorted_array

"""
$ python time_comparsion.py

[0, 1, 2, 3, 4, <rest of 10000 elements>, 9995, 9996, 9997, 9998, 9999]
Radix sort	time taken: 0.016460418701171875
Quick sort	time taken: 0.016669750213623047
Shell sort	time taken: 0.028717994689941406
Selection sort	time taken: 2.172793388366699
Insertion sort	time taken: 3.411729574203491
Bubble sort	time taken: 6.132898569107056
Counting sort	time taken: 6.209801912307739

"""
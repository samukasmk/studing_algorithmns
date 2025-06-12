from heapq import heappush, heappop


def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


unsorted_items = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
sorted_items = heapsort(unsorted_items)

print('unsorted items:', unsorted_items)
print('sorted items:', sorted_items)
print()
# unsorted items: [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# sorted items: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


h = []
heappush(h, (5, 'write code'))
heappush(h, (7, 'release product'))
heappush(h, (1, 'write spec'))
heappush(h, (3, 'create tests'))

print('heap object:', h)
print()
# heap object: [(1, 'write spec'), (3, 'create tests'), (5, 'write code'), (7, 'release product')]

i = heappop(h)
print('current item:', i)
print('current heap:', h)
print()
# current item: (1, 'write spec')
# current heap: [(3, 'create tests'), (7, 'release product'), (5, 'write code')]

i = heappop(h)
print('current item:', i)
print('current heap:', h)
print()
# current item: (3, 'create tests')
# current heap: [(5, 'write code'), (7, 'release product')]

i = heappop(h)
print('current item:', i)
print('current heap:', h)
print()
# current item: (5, 'write code')
# current heap: [(7, 'release product')]

i = heappop(h)
print('current item:', i)
print('current heap:', h)
print()
# current item: (7, 'release product')
# current heap: []

i = heappop(h)
# Traceback (most recent call last):
#   File ".../studing_algorithmns/data_structures/heaps/python_heapq.py", line 54, in <module>
#     i = heappop(h)
# IndexError: index out of range

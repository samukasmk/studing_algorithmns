"""
From book: Data Structures and Algorithms in Python
Developed by: Michael T. Goodrich, Roberto Tamassia and Michael H. Goldwasser
Chapter: 5.3.1 - Implementing a Dynamic Array
Where to buy the book: https://www.amazon.com.br/dp/1118290275
"""

import pytest
import ctypes


class DinamicArray:
    """ A dinamic array class akin to a simplified Python list. """

    def __init__(self):
        # count actual elements
        self._n = 0
        # default array capacity
        self._capacity = 1
        # low-level array
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """ Return number of elements stored in array """
        return self._n

    def __getitem__(self, k):
        """ Return element at index k. """
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        # retrieve from array
        return self._A[k]

    def append(self, obj):
        """ Add object to end of the array. """

        # not enough room
        if self._n == self._capacity:
            # so double capacity
            self._resize(2 * self._capacity)

        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """ Resize internal array to capacity c. """

        # new (bigger) array
        B = self._make_array(c)

        # for each existing value
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """ Return new array with capacity c. """
        # see ctypes documentation
        return (c * ctypes.py_object)()


class TestDinamicArray:

    def setup_method(self):
        self.dinamic_array = DinamicArray()
        for i in range(10, 21):
            self.dinamic_array.append(i)

    @pytest.mark.parametrize("expected_index, expected_item",
                             ((index, item) for index, item in enumerate(range(10, 21))))
    def test_array_get(self, expected_index, expected_item):
        assert self.dinamic_array[expected_index] == expected_item


if __name__ == "__main__":
    import os
    import pytest

    current_file = os.path.abspath(__file__)
    pytest.main([current_file])

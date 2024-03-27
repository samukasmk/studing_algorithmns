from typing import Any, Iterable
from ctypes import py_object

from array import array
class ExpansibleArray:

    def __init__(self, available_slots: int = 10, initial_elements: Iterable | None = None):
        self.__total_elements = 0
        self.__available_slots = available_slots
        self.__data_structure = self.__create_data_structure(available_slots)

        # normalize initial_elements to empty list if is not set on __init__
        if initial_elements is None:
            initial_elements = []

        # check if initial_elements is bigger than available_slots
        total_initial_elements = len(initial_elements)
        if total_initial_elements > available_slots:
            raise Exception("There are more initial_values elements than available slots in this structure!")

        # fill current data structure with initial_elements
        for slot_index in range(total_initial_elements):
            self.__data_structure[slot_index] = initial_elements[slot_index]
            self.__total_elements += 1

    # magic methods
    def __len__(self):
        return self.__total_elements

    def __getitem__(self, index_position: int) -> py_object:
        # check element existence
        if index_position >= self.__total_elements:
            raise IndexError(f'This array has just {self.__total_elements} elements!')
        return self.__data_structure[index_position]

    def __setitem__(self, index_position: int, value: Any):
        # check if desired index_position is until the next element
        if index_position > self.__total_elements:
            raise IndexError(f'You can set to the next free slot index ({self.__total_elements})!')
        # increment counter if is a new element
        elif index_position == self.__total_elements:
            self.__total_elements += 1
        self.__data_structure[index_position] = value

    def append(self, value):
        # expand slots structure in case of crowding elements
        if self.__total_elements == self.__available_slots:
            self.__resize_data_structure_slots()

        # assign new value to desired position
        self.__data_structure[self.__total_elements] = value

        # increment count of existent elements
        self.__total_elements += 1

    # data structure logic

    @staticmethod
    def __create_data_structure(fixed_slots: int) -> py_object:
        return (py_object * fixed_slots)()

    def __resize_data_structure_slots(self):
        # increase new block size slots
        self.__available_slots += self.__total_elements

        # create new empty data structure
        new_data_structure = self.__create_data_structure(self.__available_slots)

        # copy data from current to new data structure
        for slot_index in range(self.__total_elements):
            new_data_structure[slot_index] = self.__data_structure[slot_index]

        # reassign current variable reference
        self.__data_structure = new_data_structure


if __name__ == '__main__':
    # create data structure
    my_array = ExpansibleArray(available_slots=10, initial_elements=(1, 2, 3))

    print('Get all elements: [Complexity O(n) - Linear]')
    for index in range(10):
        try:
            print(f'-> my_array[{index}] =', my_array[index])
        except IndexError as exc:
            print(f'-> my_array[{index}] = Element not found! [IndexError: {exc}]')

    print('---')
    print('Get existing element: [Complexity O(1) - Constant]')
    print('-> my_array[2] =', my_array[2])

    print('---')
    print('Set existing element: [Complexity O(1) - Constant]')
    my_array[2] = 100
    print('-> my_array[2] =', my_array[2])

    print('---')
    print('Append new element: [Complexity O(1) - Constant]')
    my_array.append(200)
    print('-> my_array[3] =', my_array[3])
























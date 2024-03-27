from typing import Any, Iterable
from ctypes import py_object


class ExpansibleArray:

    def __init__(self, available_slots: int = 10, initial_elements: Iterable | None = None):
        self.__total_elements = 0
        self.__available_slots = available_slots
        self.__data_structure = self.__create_data_structure(available_slots)
        self.__populate_initial_elements(initial_elements)

    #
    # private methods
    #
    @staticmethod
    def __create_data_structure(fixed_slots: int) -> py_object:
        return (py_object * fixed_slots)()

    def __populate_initial_elements(self, initial_elements: Iterable | None = None):
        # normalize initial_elements to empty list if is not set on __init__
        if initial_elements is None:
            initial_elements = []

        # check if initial_elements is bigger than available_slots
        total_initial_elements = len(initial_elements)
        if total_initial_elements > self.__available_slots:
            raise Exception("There are more initial_values elements than available slots in this structure!")

        # fill current data structure with initial_elements
        for slot_index in range(total_initial_elements):
            self.__data_structure[slot_index] = initial_elements[slot_index]
            self.__total_elements += 1

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

    def __raise_error_if_element_not_found(self, index_position, exception_message):
        if index_position >= self.__total_elements:
            raise IndexError(exception_message)

    #
    # magic methods
    #
    def __getitem__(self, index_position: int) -> py_object:
        """
        Complexity: O(1) - Constant

        >>> my_array[2]
        "element stored"
        >>> my_array[1000]
        IndexError: list index out of range
        """
        # check element existence
        self.__raise_error_if_element_not_found(index_position, 'list index out of range')
        # return element by index slot position
        return self.__data_structure[index_position]

    def __setitem__(self, index_position: int, value: Any):
        """
        Complexity: O(1) - Constant

        >>> my_array[2] = "new element stored"
        "new element stored"
        >>> my_array[1000] = "other element"
        IndexError: list assignment index out of range
        """
        # check element existence
        self.__raise_error_if_element_not_found(index_position, 'list assignment index out of range')
        # set new value for existing slot
        self.__data_structure[index_position] = value

    def __len__(self):
        """
        Return total of existing elements in current data structure
        Complexity: O(1) - Constant
        """
        return self.__total_elements

    def __iter__(self):
        """ Iterate all elements - Complexity: O(n) - Linear"""
        for index_position in range(self.__total_elements):
            yield self.__data_structure[index_position]

    #
    # public
    #
    def append(self, value):
        # expand slots structure in case of crowding elements
        if self.__total_elements == self.__available_slots:
            self.__resize_data_structure_slots()

        # assign new value to desired position
        self.__data_structure[self.__total_elements] = value

        # increment count of existent elements
        self.__total_elements += 1


if __name__ == '__main__':
    # create data structure
    print('---')
    print('Creating data structure (with initial values): [Complexity O(n) - Linear]')
    print('>>> my_array = ExpansibleArray(available_slots=10, initial_elements=("A", "B", "C"))')
    my_array = ExpansibleArray(available_slots=10, initial_elements=("A", "B", "C"))

    print('\nWhere:')
    print('-> In slot position: 0 - Has (str) element: "A"')
    print('-> In slot position: 1 - Has (str) element: "B"')
    print('-> In slot position: 2 - Has (str) element: "C"')

    print('\n---')
    print('Get existing element: [Complexity O(1) - Constant]')
    print('>>> my_array[1]')
    print(my_array[1])

    print('\n---')
    print('Get non existing element: [Complexity O(1) - Constant]')
    try:
        my_array[1000]
    except IndexError as exc:
        print(f'-> my_array[1000]')
        print(f'IndexError: {exc}')

    print('\n---')
    print('Set existing element: [Complexity O(1) - Constant]')
    print('>>> my_array[2] = "Y"')
    my_array[2] = "Y"
    print('>>> my_array[2]')
    print(my_array[2])

    print('\n---')
    print('Set non existing element: [Complexity O(1) - Constant]')
    try:
        my_array[1000] = 1000
    except IndexError as exc:
        print(f'-> my_array[1000] = 1000\nIndexError: {exc}')

    print('\n---')
    print('Append new element: [Complexity O(1) - Constant]')
    print('>>> my_array.append("Z")')
    my_array.append("Z")
    print('>>> my_array[3] =', my_array[3])

    print('\n---')
    print('Get all elements: [Complexity O(n) - Linear]')
    index_counter = 0
    for element in my_array:
        print(f'>>> my_array[{index_counter}]')
        print(element)
        index_counter += 1

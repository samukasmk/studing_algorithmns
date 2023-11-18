from typing import List, Any


class UnkwownMethodOnAppendAction(Exception):
    ...


class NodeElement:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class SamukaLinkedList:
    def __init__(self, initial_elements: Any = None):
        self.head = None
        self.tail = None
        self.__size = 0
        if initial_elements is not None:
            self.__append_initial_elements(initial_elements)

    ### size features
    @property
    def size(self) -> None:
        """ Count how much elements has in this data structure """
        return self.__size

    def __count_new_element(self) -> None:
        """ Add one more element on count """
        self.__size += 1

    def __count_removed_element(self) -> None:
        """ Remove one more element from count """
        self.__size -= 1

    def __len__(self) -> int:
        """ Magic method for python return the length of this object """
        return self.size

    def get_positive_index(self, element_index: int) -> int:
        print(self.size)
        """ Convert element index to positive position """
        if element_index < 0:
            element_index = self.size + element_index
        return element_index

    ### append features
    def append(self, element_value):
        """ Append new element as the last item if the Linked List """
        self.append_in_tail(element_value)

    def append_in_tail(self, element_value):
        new_last_element = NodeElement(value=element_value)
        # defining the first element
        if self.head is None:
            self.head = new_last_element
        # redefining the last element
        if self.tail is not None:
            self.tail.next_node = new_last_element
        self.tail = new_last_element
        # adding more one on count
        self.__count_new_element()

    def append_in_head(self, element_value):
        new_first_element = NodeElement(value=element_value, next_node=self.head)
        self.head = new_first_element
        # adding more one on count
        self.__count_new_element()

    def __append_initial_elements(self, initial_elements: List[Any]) -> None:
        """ Append initial values """
        for initial_element in initial_elements:
            self.append_in_tail(initial_element)

    ### get features
    def __raise_exception_if_is_empty(self) -> None:
        if self.head is None:
            raise IndexError('This list is empty')

    def get_element_by_index(self, element_index: int) -> NodeElement:
        """ Return the value of desired node element by index """
        self.__raise_exception_if_is_empty()

        # convert negative index into positive numbers
        element_index = self.get_positive_index(element_index)

        # set initial node as head reference
        current_node = self.head

        # go forward on next elements according to index received
        for _ in range(element_index):

            # check if current node is defined or if doesn't exist the desired index
            if current_node is None:
                raise IndexError(f'This list just have {self.size} elements')

            # go forward to the next existing node
            current_node = current_node.next_node

        # returns found NodeElement
        return current_node

    def __getitem__(self, element_index):
        return self.get_element_by_index(element_index).value

    ### set features
    def set_element_by_index(self, element_index: int, element_value: Any) -> None:
        """ Change current node element for a new object """

        # convert negative index into positive numbers
        element_index = self.get_positive_index(element_index)

        # replace value of the existing node element
        node_element = self.get_element_by_index(element_index)
        node_element.value = element_value

    def __setitem__(self, element_index, element_value):
        return self.set_element_by_index(element_index, element_value)

    ### insert features
    def insert(self, index_position: int, element_value: Any) -> None:
        """ Insert new element in position of an existing element """
        self.__raise_exception_if_is_empty()

        # convert negative index into positive numbers
        index_position = self.get_positive_index(index_position)
        print(index_position)
        # get current and previous node
        current_node = self.head
        previous_node = None

        for _ in range(index_position):
            if current_node is None:
                raise IndexError(f'This list just have {self.size} elements')

            previous_node = current_node
            current_node = current_node.next_node

        # insert new node
        new_element = NodeElement(element_value, next_node=current_node)

        if index_position == 0:
            self.head = new_element
        else:
            previous_node.next_node = new_element

        # adding more one on count
        self.__count_new_element()

    def to_str(self):
        """ Returns a string representation of a linked nodes in lists """
        # append initial left bracket
        str_object = '['
        # count index found
        index = 0
        # get initial element
        actual_node = self.head
        while actual_node is not None:
            # append to string the index and node __str__ of value
            str_object += f"({index}: {actual_node.value}), "
            actual_node = actual_node.next_node
            # increment index count
            index += 1
        # remove final comma
        str_object = str_object.rstrip(', ')
        # append final right bracket
        str_object += ']'
        return str_object

    def __repr__(self):
        return self.to_str()

    def __str__(self):
        return self.to_str()

    ### remove features

    ### search features


### Pytest: Fixtures
import pytest


@pytest.fixture()
def empty_linked_list():
    return SamukaLinkedList()


@pytest.fixture()
def linked_list():
    return SamukaLinkedList(initial_elements=['First element', 'Second element', 'Third element', 'Fourth element'])


### Pytest: Tests
class TestSamukaLinkedList:
    def test_empty_list_creation(self, empty_linked_list):
        assert len(empty_linked_list) == 0
        assert empty_linked_list.head is None
        assert empty_linked_list.tail is None

    def test_normal_list_creation(self, linked_list):
        assert len(linked_list) == 4
        assert linked_list.head is not None
        assert linked_list.head.value == 'First element'
        assert linked_list.head.next_node is not None
        assert linked_list.head.next_node.value == 'Second element'
        assert linked_list.head.next_node.next_node is not None
        assert linked_list.head.next_node.next_node.value == 'Third element'
        assert linked_list.head.next_node.next_node.next_node is not None
        assert linked_list.head.next_node.next_node.next_node.value == 'Fourth element'
        assert linked_list.tail is not None
        assert linked_list.tail.value == 'Fourth element'

    def test_append_element_in_default(self, linked_list):
        linked_list.append(10)
        assert len(linked_list) == 5
        assert linked_list.tail is not None
        assert linked_list.tail.value == 10

    def test_append_element_in_tail(self, linked_list):
        linked_list.append_in_tail(4)
        assert len(linked_list) == 5
        assert linked_list.tail is not None
        assert linked_list.tail.value == 4

    def test_append_element_in_head(self, linked_list):
        linked_list.append_in_head(0)
        assert len(linked_list) == 5
        assert linked_list.head is not None
        assert linked_list.head.value == 0

    def test_insert_new_element_in_the_begin(self, linked_list):
        assert len(linked_list) == 4
        linked_list.insert(1, 'Third position')
        assert len(linked_list) == 5
        assert linked_list.head is not None
        assert linked_list.head.next_node is not None
        assert linked_list.head.next_node.value == 'Third position'

    def test_insert_new_element_in_the_middle(self, linked_list):
        assert len(linked_list) == 4
        linked_list.insert(3, 'Fourth position')
        assert len(linked_list) == 5
        assert linked_list.head is not None
        assert linked_list.head.next_node is not None
        assert linked_list.head.next_node.next_node is not None
        assert linked_list.head.next_node.next_node.next_node is not None
        assert linked_list.head.next_node.next_node.next_node.value == 'Fourth position'

    def test_insert_new_element_in_the_last_positive(self, linked_list):
        assert len(linked_list) == 4
        linked_list.insert(4, 'Last position')
        assert len(linked_list) == 5
        assert linked_list.head is not None
        assert linked_list.head.next_node is not None
        assert linked_list.head.next_node.next_node is not None
        assert linked_list.head.next_node.next_node.next_node is not None
        assert linked_list.head.next_node.next_node.next_node.next_node is not None
        assert linked_list.head.next_node.next_node.next_node.next_node.value == 'Last position'

    def test_insert_new_element_index_error(self, linked_list):
        assert len(linked_list) == 4
        with pytest.raises(IndexError):
            linked_list.insert(5, 'Last position')

    @pytest.mark.parametrize("existing_index, existing_element", (
            (0, 'First element'),
            (1, 'Second element'),
            (2, 'Third element'),
            (3, 'Fourth element')))
    def test_get_existing_element_by_index(self, existing_index, existing_element, linked_list):
        assert linked_list.get_element_by_index(existing_index).value == existing_element
        assert linked_list[existing_index] == existing_element

    def test_get_non_existing_element_in_filled_list(self, linked_list):
        with pytest.raises(IndexError):
            linked_list.get_element_by_index(1000)
        with pytest.raises(IndexError):
            linked_list[10000]

    def test_get_non_existing_element_in_empty_list(self, empty_linked_list):
        with pytest.raises(IndexError):
            empty_linked_list.get_element_by_index(0)
        with pytest.raises(IndexError):
            empty_linked_list[0]

    def test_set_existing_element_by_index(self, linked_list):
        assert linked_list[1] == 'Second element'
        linked_list[1] = 'Changed element'
        assert linked_list[1] == 'Changed element'

    def test_set_non_existing_element_in_filled_list(self, linked_list):
        with pytest.raises(IndexError):
            linked_list.set_element_by_index(1000, 42)
        with pytest.raises(IndexError):
            linked_list[10000] = 42

    def test_set_non_existing_element_in_empty_list(self, empty_linked_list):
        with pytest.raises(IndexError):
            empty_linked_list.set_element_by_index(0, 'non existing index')
        with pytest.raises(IndexError):
            empty_linked_list[0] = 'non existing index'

    def test_remove_first_element(self):
        del linked_list[0]

    def test_remove_middle_element(self):
        del linked_list[1]

    def test_remove_last_element(self):
        del linked_list[2]

    def test_remove_non_existing_element(self):
        with pytest.raises(IndexError):
            del linked_list[10000]

    @pytest.mark.parametrize("existing_element", (
            'First element',
            'Second element',
            'Third element',
            'Fourth element'))
    def test_search_existing_element_in_list(self, existing_element):
        assert existing_element in linked_list

    def test_search_non_existing_element_in_list(self):
        assert 'Non existing element' in linked_list is False

    def test_to_str_representation(self, linked_list):
        expected_string = '[(0: First element), (1: Second element), (2: Third element), (3: Fourth element)]'
        assert linked_list.to_str() == expected_string
        assert str(linked_list) == expected_string
        assert repr(linked_list) == expected_string


if __name__ == '__main__':
    import os
    import pytest

    current_file = os.path.abspath(__file__)
    pytest.main([current_file])

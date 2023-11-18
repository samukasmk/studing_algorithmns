from typing import List, Any


class UnkwownMethodOnAppendAction(Exception):
    ...


class NodeElement:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


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

    @property
    def is_empty(self) -> bool:
        """ Check if list is empty """
        return self.size == 0

    def is_an_existing_index(self, index_position: int) -> bool:
        """ Check if there is a position by index"""
        return not self.is_empty and (index_position + 1) > self.size
    def __fail_if_index_doesnt_exist(self, index_position: int) -> None:
        """ raise IndexError exception if user wants to get an non existent element """
        if not self.is_an_existing_index(index_position):
            raise IndexError(f'This list just have {self.size} elements')

    def __count_new_element(self) -> None:
        """ Add one more element on count """
        self.__size += 1

    def __count_removed_element(self) -> None:
        """ Remove one more element from count """
        self.__size -= 1

    def __len__(self) -> int:
        """ Magic method for python return the length of this object """
        return self.size

    def __get_positive_index(self, index_position: int) -> int:
        print(self.size)
        """ Convert element index to positive position """
        if index_position < 0:
            index_position = self.size + index_position
        return index_position

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
            self.tail.next = new_last_element
        self.tail = new_last_element
        # adding more one on count
        self.__count_new_element()

    def append_in_head(self, element_value):
        new_first_element = NodeElement(value=element_value, next=self.head)
        self.head = new_first_element
        # adding more one on count
        self.__count_new_element()

    def __append_initial_elements(self, initial_elements: List[Any]) -> None:
        """ Append initial values """
        for initial_element in initial_elements:
            self.append_in_tail(initial_element)

    ### get features
    def __raise_exc_if_is_empty(self) -> None:
        if self.head is None:
            raise IndexError('This list is empty')


    def get_element_by_index(self, element_index: int) -> NodeElement:
        """ Return the value of desired node element by index """
        self.__raise_exc_if_is_empty()

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
            current_node = current_node.next

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

        self.__fail_if_index_doesnt_exist(index_position)

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
            current_node = current_node.next

        # insert new node
        new_element = NodeElement(element_value, next=current_node)

        if index_position == 0:
            self.head = new_element
        else:
            previous_node.next = new_element

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
            actual_node = actual_node.next
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

    ### delete features
    def delete(self, index_position):
        """ Delete a node element from list """
        self.__fail_if_index_doesnt_exist(index_position)

        # iterate node elements
        current = self.head
        previous = None
        for _ in range(index_position):
            if current is None:
                raise IndexError(f'This list just have {self.size} elements')
            previous = current
            current = current.next

        # update head reference
        if index_position == 0:
            self.head = current.next

        # skip current node link previous with next
        if previous and current:
            previous.next = current.next

        # or unlink if it'll be the last element
        elif previous:
            previous.next = None

        # remove node from memory
        del current

        # mark in counter as removed
        self.__count_removed_element()

    def __delitem__(self, index_position):
        self.delete(index_position)

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
        assert linked_list.head.next is not None
        assert linked_list.head.next.value == 'Second element'
        assert linked_list.head.next.next is not None
        assert linked_list.head.next.next.value == 'Third element'
        assert linked_list.head.next.next.next is not None
        assert linked_list.head.next.next.next.value == 'Fourth element'
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
        assert linked_list.head.next is not None
        assert linked_list.head.next.value == 'Third position'

    def test_insert_new_element_in_the_middle(self, linked_list):
        assert len(linked_list) == 4
        linked_list.insert(3, 'Fourth position')
        assert len(linked_list) == 5
        assert linked_list.head is not None
        assert linked_list.head.next is not None
        assert linked_list.head.next.next is not None
        assert linked_list.head.next.next.next is not None
        assert linked_list.head.next.next.next.value == 'Fourth position'

    def test_insert_new_element_in_the_last_positive(self, linked_list):
        assert len(linked_list) == 4
        linked_list.insert(4, 'Last position')
        assert len(linked_list) == 5
        assert linked_list.head is not None
        assert linked_list.head.next is not None
        assert linked_list.head.next.next is not None
        assert linked_list.head.next.next.next is not None
        assert linked_list.head.next.next.next.next is not None
        assert linked_list.head.next.next.next.next.value == 'Last position'

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

    def test_delete_elements(self):
        linked_list = SamukaLinkedList([0, 1, 2, 3])
        assert len(linked_list) == 4

        # [0, 1, 2, 3]
        assert linked_list[0] == 0
        assert linked_list[1] == 1
        assert linked_list[2] == 2
        assert linked_list[3] == 3

        del linked_list[0]
        assert len(linked_list) == 3
        # [1, 2, 3]
        assert linked_list[0] == 1
        assert linked_list[1] == 2
        assert linked_list[2] == 3
        # check get operations
        with pytest.raises(IndexError):
            linked_list[3]
        # del operations
        with pytest.raises(IndexError):
            del linked_list[3]

        del linked_list[2]
        assert len(linked_list) == 2
        # [1, 2]
        assert linked_list[0] == 1
        assert linked_list[1] == 2
        # check get operations
        with pytest.raises(IndexError):
            linked_list[2]
        with pytest.raises(IndexError):
            linked_list[3]
        # del operations
        with pytest.raises(IndexError):
            del linked_list[2]
        with pytest.raises(IndexError):
            del linked_list[3]

        del linked_list[1]
        assert len(linked_list) == 1
        # [1]
        assert linked_list[0] == 1
        # check get operations
        with pytest.raises(IndexError):
            linked_list[1]
        with pytest.raises(IndexError):
            linked_list[2]
        with pytest.raises(IndexError):
            linked_list[3]
        # del operations
        with pytest.raises(IndexError):
            del linked_list[1]
        with pytest.raises(IndexError):
            del linked_list[2]
        with pytest.raises(IndexError):
            del linked_list[3]

        del linked_list[0]
        assert len(linked_list) == 0
        # check get operations
        with pytest.raises(IndexError):
            linked_list[0]
        with pytest.raises(IndexError):
            linked_list[1]
        with pytest.raises(IndexError):
            linked_list[2]
        with pytest.raises(IndexError):
            linked_list[3]
        # del operations
        with pytest.raises(IndexError):
            del linked_list[0]
        with pytest.raises(IndexError):
            del linked_list[1]
        with pytest.raises(IndexError):
            del linked_list[2]
        with pytest.raises(IndexError):
            del linked_list[3]
    def test_delete_middle_element(self):
        del linked_list[1]

    def test_delete_last_element(self):
        del linked_list[2]

    def test_delete_non_existing_element(self):
        with pytest.raises(IndexError):
            del linked_list[10000]

    def test_remove_element_by_linear_search(self):
        existing_elements = ['First element', 'Second element', 'Third element', 'Fourth element']
        for existing_index, existing_element in existing_elements:
            assert len(linked_list) == 4
            assert linked_list[existing_index] == existing_element

            linked_list.remove(existing_element)
            assert len(linked_list) == 3

            last_index = len(existing_elements) - 1
            next_index = existing_index + 1
            if next_index < last_index:
                assert linked_list[existing_index] == existing_elements[next_index]

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

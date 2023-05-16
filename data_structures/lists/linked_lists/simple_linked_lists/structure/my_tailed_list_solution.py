from typing import List, Any


class UnkwownMethodOnAppendAction(Exception):
    ...


class NodeElement:
    def __init__(self, value, next_node_element=None):
        self.value = value
        self.next_node_element = next_node_element


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

    ### append features
    def __append_initial_elements(self, initial_elements: List[Any]) -> None:
        """ Append initial values """
        for initial_element in initial_elements:
            self.append_in_tail(initial_element)

    def append(self, element):
        """ Append new element as the last item if the Linked List """
        self.append_in_tail(element)

    def append_in_tail(self, element):
        new_last_element = NodeElement(value=element)
        # defining the first element
        if self.head is None:
            self.head = new_last_element
        # redefining the last element
        if self.tail is not None:
            self.tail.next_node_element = new_last_element
        self.tail = new_last_element
        # adding more one on count
        self.__count_new_element()

    def append_in_head(self, element):
        new_first_element = NodeElement(value=element, next_node_element=self.head)
        self.head = new_first_element
        # adding more one on count
        self.__count_new_element()

    ### get features
    def get_element_by_index(self, index: int) -> Any:
        """ Returns the value of desired node element by index """
        if self.head is None:
            raise IndexError('This list is empty')

        # set initial node as head reference
        current = self.head

        # go forward on next elements according to index received
        for _ in range(index):
            # check if current node is defined or if doesn't exist the desired index
            if current is None:
                raise IndexError(f'This list just have {self.size} elements')
            # go forward to the next existing node
            current = current.next_node_element


        # returns the value
        return current.value

    def __getitem__(self, item):
        return self.get_element_by_index(item)

    ### insert features

    ### remove features

    ### search features


### Pytest: Fixtures
import pytest


@pytest.fixture()
def empty_linked_list():
    return SamukaLinkedList()


@pytest.fixture()
def linked_list():
    return SamukaLinkedList(initial_elements=[1, 'Second element', 3.6])


### Pytest: Tests
class TestSamukaLinkedList:
    def test_empty_list_creation(self, empty_linked_list):
        assert len(empty_linked_list) == 0
        assert empty_linked_list.head is None
        assert empty_linked_list.tail is None

    def test_normal_list_creation(self, linked_list):
        assert linked_list.head.value == 1
        assert len(linked_list) == 3
        assert linked_list.tail is not None
        assert linked_list.tail.value == 3.6

    def test_append_element_in_default(self, linked_list):
        linked_list.append(element=10)
        assert len(linked_list) == 4
        assert linked_list.tail is not None
        assert linked_list.tail.value == 10

    def test_append_element_in_tail(self, linked_list):
        linked_list.append_in_tail(element=4)
        assert len(linked_list) == 4
        assert linked_list.tail is not None
        assert linked_list.tail.value == 4

    def test_append_element_in_head(self, linked_list):
        linked_list.append_in_head(element=0)
        assert len(linked_list) == 4
        assert linked_list.head is not None
        assert linked_list.head.value == 0

    def test_insert_middle_element(self):
        linked_list.insert(position=3, element='Third position')
        assert len(linked_list) == 4
        assert linked_list.head is not None
        assert linked_list.head.next_node_element is not None
        assert linked_list.head.next_node_element.next_node_element is not None
        assert linked_list.head.next_node_element.next_node_element.value == 'Third position'

    @pytest.mark.parametrize("existing_index, existing_element", [(0, 1), (1, 'Second element'), (2, 3.6)])
    def test_get_existing_element_by_index(self, existing_index, existing_element, linked_list):
        assert linked_list.get_element_by_index(existing_index) == existing_element
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
            empty_linked_list.set_element_by_index(1000, 42)
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

    @pytest.mark.parametrize("existing_elements", [1, 'Second element', 3.6])
    def test_search_existing_element_in_list(self, existing_elements):
        for existing_element in existing_elements:
            assert existing_element in linked_list

    def test_search_non_existing_element_in_list(self):
        assert 'Non existing element' in linked_list is False


if __name__ == '__main__':
    import os
    import pytest

    current_file = os.path.abspath(__file__)
    pytest.main([current_file])

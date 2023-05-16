from typing import List, Any


class UnkwownMethodOnAppendAction(Exception):
    ...


class NodeElement:
    def __init__(self, value, next_element=None):
        self.value = value
        self.next_element = next_element


class SamukaLinkedList:
    def __init__(self, initial_elements: Any = None):
        self.head = None
        self.tail = None
        self.__size = 0
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
            self.tail.next = new_last_element
        self.tail = new_last_element
        # adding more one on count
        self.__count_new_element()

    def append_in_head(self, element):
        new_first_element = NodeElement(value=element, next_element=self.head)
        self.head = new_first_element
        # adding more one on count
        self.__count_new_element()

    ### get features

    ### insert features

    ### remove features

    ### search features


### Pytest: Fixtures
import pytest


@pytest.fixture()
def linked_list():
    linked_list = SamukaLinkedList(initial_elements=[1, 'Second element', 3.6])
    assert linked_list.head.value == 1
    assert len(linked_list) == 3
    return linked_list


### Pytest: Tests
class TestSamukaLinkedList:
    def test_empty_list_creation(self):
        linked_list = SamukaLinkedList(initial_elements=[])
        assert len(linked_list) == 0
        assert linked_list.head is None
        assert linked_list.tail is None

    def test_normal_list_creation(self, linked_list):
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
        assert linked_list.head.next is not None
        assert linked_list.head.next.next is not None
        assert linked_list.head.next.next.value == 'Third position'

    @pytest.mark.parametrize("existing_elements", [1, 'Second element', 3.6])
    def test_get_element_by_index(self, existing_elements, linked_list):
        for existing_index, existing_element in enumerate(existing_elements):
            assert linked_list[existing_index] == existing_element

    def test_get_non_existing_element(self):
        with pytest.raises(IndexError):
            linked_list[10000]

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

"""
From book: Data Structures and Algorithms with Python
Developed by: Kent D. Lee and Steve Hubbard
Chapter: 4.1. - The PyList Datatype
Where to buy the book: https://www.amazon.com.br/dp/3319130714
Source code: https://kentdlee.github.io/CS2Plus/build/html/chap4/chap4.html#the-pylist-datatype
"""


class PyList:
    def __init__(self, contents=[], size=10):
        # The contents allows the programmer to construct a list with
        # the initial contents of this value. The initial_size
        # lets the programmer pick a size for the internal size of the 
        # list. This is useful if the programmer knows he/she is going 
        # to add a specific number of items right away to the list.
        self.items = [None] * size
        self.numItems = 0
        self.size = size

        for e in contents:
            self.append(e)

    def __getitem__(self, index):
        if index < self.numItems:
            return self.items[index]

        raise IndexError("PyList index out of range")

    def __setitem__(self, index, val):
        if index < self.numItems:
            self.items[index] = val
            return

        raise IndexError("PyList assignment index out of range")

    def insert(self, i, e):
        if self.numItems == self.size:
            self.__makeroom()

        if i < self.numItems:
            for j in range(self.numItems - 1, i - 1, -1):
                self.items[j + 1] = self.items[j]

            self.items[i] = e
            self.numItems += 1
        else:
            self.append(e)

    def __add__(self, other):
        result = PyList()

        for i in range(self.numItems):
            result.append(self.items[i])

        for i in range(other.numItems):
            result.append(other.items[i])

        return result

    def __contains__(self, item):
        for i in range(self.numItems):
            if self.items[i] == item:
                return True

        return False

    def __delitem__(self, index):
        for i in range(index, self.numItems - 1):
            self.items[i] = self.items[i + 1]
        self.numItems -= 1  # same as writing self.numItems = self.numItems - 1

    def __eq__(self, other):
        if type(other) != type(self):
            return False

        if self.numItems != other.numItems:
            return False

        for i in range(self.numItems):
            if self.items[i] != other.items[i]:
                return False

        return True

    def __iter__(self):
        for i in range(self.numItems):
            yield self.items[i]

    def __len__(self):
        return self.numItems

    # This method is hidden since it starts with two underscores. 
    # It is only available to the class to use. 
    def __makeroom(self):
        # increase list size by 1/4 to make more room.
        newlen = (self.size // 4) + self.size + 1
        newlst = [None] * newlen
        for i in range(self.numItems):
            newlst[i] = self.items[i]

        self.items = newlst
        self.size = newlen

    def append(self, item):
        if self.numItems == self.size:
            self.__makeroom()

        self.items[self.numItems] = item
        self.numItems += 1  # Same as writing self.numItems = self.numItems + 1

    def __str__(self):
        s = "["
        for i in range(self.numItems):
            s = s + str(self.items[i])
            if i < self.numItems - 1:
                s = s + ", "
        s = s + "]"
        return s

    def __repr__(self):
        s = "PyList(["
        for i in range(self.numItems):
            s = s + str(self.items[i])
            if i < self.numItems - 1:
                s = s + ", "
        s = s + "])"
        return s

    def sort(self):
        pass


class TestPyListOperations():
    def setup_method(self):
        # first case
        self.lst = PyList()
        for i in range(100):
            self.lst.append(i)
        # second case
        self.lst2 = PyList(self.lst)
        # third case
        self.lst3 = self.lst + self.lst2
        # fourth case
        self.lst4 = PyList(self.lst)
        self.lst4 = PyList([100]) + self.lst4

    def test_eq_operation(self):
        assert self.lst == self.lst2

    def test_add_operation(self):
        assert len(self.lst3) == len(self.lst) + len(self.lst2)

    def test_contains_operation(self):
        assert 1 in self.lst3
        assert 2 in self.lst3

    def test_del_operation(self):
        del self.lst[1]
        assert 1 not in self.lst

    def test_len_operation(self):
        assert len(self.lst) == 100
        del self.lst[1]
        assert len(self.lst) == 99

    def test_insert_operation(self):
        self.lst.insert(0, 100)
        assert self.lst == self.lst4

    def test_append_operation(self):
        self.lst.insert(0, 100)
        self.lst.insert(1000, 333)
        self.lst4.append(333)
        assert self.lst == self.lst4


if __name__ == "__main__":
    import os
    import pytest

    current_file = os.path.abspath(__file__)
    pytest.main([current_file])

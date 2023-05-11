"""
From book: Data Structures and Algorithms with Python
Developed by: Michael T. Goodrich | Roberto Tamassia | Michael H. Goldwasser
Chapter: 7.2 - Circularly Linked Lists
Book link: https://amz.run/6g9I
"""


class Empty(Exception):
    ...

class CircularlyLinkedList():
    class Node():
        __slots__ = '_element', '_next'
        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """ Get next element on round-robin pattern """
        if self.is_empty():
            raise Empty('CircularlyLinkedList is empty')
        head = self.tail.next
        return head._element

    def rotate(self):
        """ Rotoates the reference of self._tail._next"""
        if not self.is_empty():
            self._tail = self._tail._next

    def enqueue(self, element):
        """ Add new element to the circularly linked list """
        newest = self._Node(element)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('CircularlyLinkedList is empty')

        old_head = self._tail._next

        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = old_head._next

        self._size -= 1

        return old_head._element

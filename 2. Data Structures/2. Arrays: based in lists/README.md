# Arrays

## Abstract Data Type (ADT)

### Countigous Arrays

Operations:

| Operation              | Description                                                                                                                                                                                                                  | Usage                                                   | Pythonic method                                                   | Runtime complexity |
| ---------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ------------------------------------------------------- |-------------------------------------------------------------------| ------------------ |
| Structure creation     | Definition of values in memory on contigous positions                                                                                                                                                                        | my_array = Array()                                      | def \_\_init\_\_(self, initial_positions=10, initial_items=None): | O(n) or o(1)       |
| Append items           | Append new items in the last position of the structure                                                                                                                                                                       | my_array.append(item=42)                                | def append(self, item):                                           | O(1)               |
| Insert items           | Insert new items in existing positions, switching other elements to the right                                                                                                                                                | my_array.insert(index=0, item=400)                      | def insert(self, index, item):                                    | O(n)               |
| Indexed Delete         | Delete a item from structure, switching other items for the left covering the empty position                                                                                                                                 | del my_array[1]<br>my_array.pop(1)                      | def \_\_delitem\_\_(self, index):                                 | O(n)               |
| Indexed get            | Get an item in the structure by the Index number, defining the correct address in memory position                                                                                                                            | my_array[1]                                             | def \_\_getitem\_\_(self, index):                                 | O(1)               |
| Indexed insert         | Change an existing item by other by Index                                                                                                                                                                                    | my_array[1] = 12                                        | def \_\_setitem\_\_(self, index, item):                           | O(1)               |
| Equality               | Checking the items by equality                                                                                                                                                                                               | my_array == other_array                                 | def \_\_eq\_\_(self, other):                                      | O(n)               |
| Iterate                | Get items one by one to use in for loops or iteration operations                                                                                                                                                             | for i in my_array:                                      | def \_\_iter\_\_(self):                                           | O(n)               |
| Length                 | Get the length of items count by a internal attribute that is managed on the operations of appending, inserting deleting                                                                                                     | len(my_array)                                           | def \_\_len\_\_(self):                                            | O(1)               |
| Concatenate            | Merging two array items in a new array                                                                                                                                                                                       | new_array = my_array + another_array                    | def \_\_add\_\_(self, other):                                     | O(n)               |
| Membership             | Searching specific item in defined array                                                                                                                                                                                     | item in my_array                                        | def \_\_contains\_\_(self, item):                                 | O(n) or (log n)    |
| Expand                 | Defining new free positions for store new items,<br>creating new array with more free positions,<br>coping items from current arrays to new,<br>assuming the new array as oficial,<br>and deleting the old array from memory | my_array.expand(new_positions=10)                       | def expand(self, new_positions):                                  | O(n)               |
| Get last and delete    | Get last item and delete it                                                                                                                                                                                                  | my_array.pop()                                          | def pop(self, index=None):                                        | O(1)               |
| Search and delete      | Search for the first occurrence of a given item in array and remove it                                                                                                                                                       | my_array.remove(1234)                                   | def remove(self, item):                                           | O(n)               |
| Merge                  | Merging two array items in a new array                                                                                                                                                                                       | my_array.extend(other_array)<br>my_array += other_array | def \_\_iadd\_\_(self, other):                                    | O(n2)              |
| Sort                   | Sorting array items with the Timsort algorithm                                                                                                                                                                               | my_array.sort()<br>sorted(my_array)                     | def \_\_lt\_\_(self, other):                                      | O(n log n)         |
| Reverse                | Reverse all positions of the array                                                                                                                                                                                           | my_array[::-1]<br>reversed(alice)                       | def \_\_reversed\_\_(self):                                       | O(n)               |
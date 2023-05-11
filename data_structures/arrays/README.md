# Arrays

## Abstract Data Type (ADT)

### Countigous Arrays

Operations:

| Operation          | Description                                                                                                              | Usage                                | Pythonic method                                                | Runtime complexity |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ | -------------------------------------------------------------- | ------------------ |
| Structure creation | Definition of values in memory on contigous positions                                                                    | my_array = Array()                   | def \_\_init\_\_(self, initial_positions=10, initial_items=None): | O(n) or o(1)       |
| Append items       | Append new items in the last position of the structure                                                                   | my_array.append(item=42)             | def append(self, item):                                        | O(1)               |
| Insert items       | Insert new items in existing positions, switching other elements to the right                                            | my_array.insert(index=0, item=400)   | def insert(self, index, item):                                 | O(n)               |
| Delete item        | Delete a item from structure, switching other items for the left covering the empty position                             | del my_array[1]                      | def \__delitem__(self, index):                                 | O(n)               |
| Indexed get        | Get an item in the structure by the Index number, defining the correct address in memory position                        | my_array[1]                          | def \__getitem__(self, index):                                 | O(1)               |
| Indexed insert     | Change an existing item by other by Index                                                                                | my_array[1] = 12                     | def \__setitem__(self, index, item):                           | O(1)               |
| Equality           | Checking the items by equality                                                                                           | my_array == other_array              | def \_\_eq\_\_(self, other):                                      | O(n)               |
| Iterate            | Get items one by one to use in for loops or iteration operations                                                         | for i in my_array:                   | def \_\_iter\_\_(self):                                           | O(n)               |
| Length             | Get the length of items count by a internal attribute that is managed on the operations of appending, inserting deleting | len(my_array)                        | def \_\_len\_\_(self):                                            | O(1)               |
| Concatenate        | Merging two array items in a new array                                                                                   | new_array = my_array + another_array | def \_\_add\_\_(self, other):                                     | O(n)               |
| Membership         | Searching specific item in defined array                                                                                 | item in my_array                     | def \_\_contains\_\_(self, item):                                 | O(n) or            |

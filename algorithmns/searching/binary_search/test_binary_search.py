from datetime import datetime
from random import randint

# creating a short list of unique elements


# Search EXISTING elements in unique short list
for existing_element in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    start = datetime.now()
    search_result = binary_search(unique_short_list, existing_element)
    assert search_result == True
    label = "FOUND" if search_result else "NOT found"
    print(f'The element ({existing_element}) was {label} in:', datetime.now() - start)

# Search NON existing elements in short list
for non_existing_element in [-5, -4, -3, -2, -1, 0, 13, 14, 15, 16, 17, 18]:
    start = datetime.now()
    search_result = binary_search(unique_short_list, non_existing_element)
    assert search_result == False
    label = "FOUND" if search_result else "NOT found"
    print(f'The element ({non_existing_element}) was {label} in:', datetime.now() - start)

# creating a short list of repeated elements
repeated_short_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 7, 8, 8, 8, 8, 9, 10, 10, 10, 10]

# Search EXISTING elements in repeated short list
for existing_element in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    start = datetime.now()
    search_result = binary_search(repeated_short_list, existing_element)
    assert search_result == True
    label = "FOUND" if search_result else "NOT found"
    print(f'The element ({existing_element}) was {label} in:', datetime.now() - start)
# Search NON existing elements in repeated short list
for non_existing_element in [-5, -4, -3, -2, -1, 0, 13, 14, 15, 16, 17, 18]:
    start = datetime.now()
    search_result = binary_search(repeated_short_list, non_existing_element)
    assert search_result == False
    label = "FOUND" if search_result else "NOT found"
    print(f'The element ({non_existing_element}) was {label} in:', datetime.now() - start)

# creating a billionaire list with duplicated elements
billionaire_array = [randint(1, 1000000) for i in range(1000000)]
billionaire_array.sort()

# Search EXISTING elements in huge list of billion elements
for existing_element in [billionaire_array[randint(0, 999999)] for i in range(101)]:
    start = datetime.now()
    search_result = binary_search(billionaire_array, existing_element)
    assert search_result == True
    label = "FOUND" if search_result else "NOT found"
    print(f'The element ({existing_element}) was {label} in:', datetime.now() - start)

# Search NON existing elements in repeated short list
for non_existing_element in [randint(-99999, 0) for i in range(51)] + [randint(999999, 9999999) for i in range(51)]:
    start = datetime.now()
    search_result = binary_search(billionaire_array, non_existing_element)
    assert search_result == False
    label = "FOUND" if search_result else "NOT found"
    print(f'The element ({existing_element}) was {label} in:', datetime.now() - start)

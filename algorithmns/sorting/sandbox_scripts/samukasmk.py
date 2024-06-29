def sorting_by_worst_performance_ever(n: list[int]) -> list[int]:
    new_array = []

    # O(n)
    while len(n) > 0:
        min_value = min(n)  # O(n)
        new_array.append(min_value)  # O(1)
        n.remove(min_value)  # O(n)

    # O(n) * O(n) = O(n^2)
    return new_array


def finding_max_by_myself(n: list[int]) -> list[int]:
    new_array = []

    while len(n):
        # get minimum value
        min_value = None
        min_index = None
        for index, value in enumerate(n):
            if min_value is None or value < min_value:
                min_value = value
                min_index = index
        # remove minimum value and append to new_array
        del n[min_index]
        new_array.append(min_value)

    # O(n) * O(n) = O(n^2)
    return new_array


def finding_max_by_myself_range(n: list[int]) -> list[int]:
    new_array = []

    while len(n):
        # get minimum value
        min_value = None
        min_index = None
        # for each value in list
        for index in range(len(n)):  # O(n)
            # get value by index
            value = n[index]
            if min_value is None or value < min_value:
                min_value = value
                min_index = index
        # remove minimum value and append to new_array
        del n[min_index]  # O(n)
        new_array.append(min_value)  # O(1)

    # O(n) * O(n) = O(n^2)
    return new_array


r = finding_max_by_myself_range([5, 2, 1, 10, 11, 1, 3, -15])
print(r)

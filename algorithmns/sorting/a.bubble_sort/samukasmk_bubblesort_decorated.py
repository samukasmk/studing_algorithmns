"""
Bubble Sort Algorithm

Complexity:
- Time: O(n^2)
- Space: O(1)
"""
from rich.console import Console
from rich.table import Table


def bubble_sort(array: list[int]) -> list[int]:
    n = len(array)

    for position in range(n - 1):
        print('[position]:', position)

        for current_index in range(n - 1 - position):
            next_index = current_index + 1

            print(f'-> Comparing (array[{current_index}]: {array[current_index]}) '
                  f'with (array[{next_index}]: {array[next_index]})')

            debug_list(numbers, current_index, next_index)

            # swap items if is greater (for ascending order) [change to less (for descending order)]
            if array[current_index] > array[next_index]:

                print(f'   -> ({array[current_index]}) Is GREATER than ({array[next_index]}): SWIPING items tough...')

                array[current_index], array[next_index] = array[next_index], array[current_index]

            else:
                print(f'   -> ({array[current_index]}) Is LESS than ({array[next_index]}): Ignoring...')


    return array


def debug_list(numbers, current_index, next_index):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta", show_lines=True)
    table.add_column("Value:")
    for n in numbers:
        table.add_column(str(n), justify="center")
    table.add_row('Position:', *[str(p) for p in range(0, len(numbers))])
    table.add_row('', *['🔁' if p in [current_index, next_index] else '' for p in range(0, len(numbers))])
    console.print(table)


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    bubble_sort(numbers)

    # check if the original list was sorted
    assert numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]

    # print the sorted list
    print(f'Sorted list: {numbers}')

    # from rich.console import Console
    # from rich.table import Table
    #
    # console = Console()
    #
    # table = Table(show_header=True, header_style="bold magenta")
    #
    # table.add_column("Positions:")
    #
    # for i in range(0, len(numbers)):
    #     table.add_column(str(i), justify="center")
    #
    # table.add_row('Values:', *[str(n) for n in numbers])
    #
    # table.add_row('', *['🔁' for n in numbers])
    #
    # console.print(table)

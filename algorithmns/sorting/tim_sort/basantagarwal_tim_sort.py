def Insertion_Sort(unsorted_list): 
    for index in range(1, len(unsorted_list)): 
        search_index = index 
        insert_value = unsorted_list[index] 
        while search_index > 0 and unsorted_list[search_index-1] > insert_value : 
            unsorted_list[search_index] = unsorted_list[search_index-1] 
            search_index -= 1 
        unsorted_list[search_index] = insert_value 
    return unsorted_list



def Merge(first_sublist, second_sublist):
    i = j = 0
    merged_list = []
    while i < len(first_sublist) and j < len(second_sublist):
        if first_sublist[i] < second_sublist[j]:
            merged_list.append(first_sublist[i])  
            i += 1  
        else:
            merged_list.append(second_sublist[j])  
            j += 1
    while i < len(first_sublist):  
        merged_list.append(first_sublist[i])  
        i += 1  
    while j < len(second_sublist):
        merged_list.append(second_sublist[j])  
        j += 1
    return merged_list


def Tim_Sort(arr, run):
    for x in range(0, len(arr), run):
        arr[x : x + run] = Insertion_Sort(arr[x : x + run]) 
    runSize = run
    
    while runSize < len(arr):
        for x in range(0, len(arr), 2 * runSize):
            arr[x : x + 2 * runSize] = Merge(arr[x : x + runSize], arr[x + runSize: x + 2 * runSize]) 
            
        runSize = runSize * 2

# arr = [4, 6, 3, 9, 2, 8, 7, 5]
# run = 2
#
#
# Tim_Sort(arr, run)
# print(arr)


if __name__ == '__main__':
    # define a list of numbers
    numbers = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]
    print(f'Initial list: {numbers}')

    # sort elements
    Tim_Sort(numbers, 1)

    # check if the original list was sorted
    if numbers == [-34, -5, -1, 0, 1, 2, 9, 10, 56, 100]:
        print(f'Sorted list: {numbers}')
    else:
        print(f"Final is not sorted: {numbers}")
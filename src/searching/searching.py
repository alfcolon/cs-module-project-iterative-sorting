def linear_search(arr, target):
    # Your code here
    arr_len = len(arr)
    index = 0
    while index < arr_len:
        if arr[index] == target:
            return index
        index += 1
    return -1   # not found

def binary_search(arr, target):
#1. Compare the item in the middle of the data set to the item we are searching for.
    start_index = 0
    end_index = len(arr) - 1
    while start_index <= end_index:
        middle_index = start_index + (end_index - 1) // 2
        middle_value = arr[middle_index]
        # If it is the same, stop. We found it and are done!
        if target == middle_value:
            return middle_index
        # Else, if the item we are searching for is LESS than the item in the middle:
        elif target < middle_value:
            # Eliminate the RHS of list. Repeat step 1 with only the LHS of list.
            end_index = middle_index - 1
        # Else, the item we are searching for is GREATER than the item in the middle:
        else:
            # Eliminate the LHS of list. Repeat step 1 with only the RHS of the list.
            start_index = middle_index + 1
    return -1  # not found

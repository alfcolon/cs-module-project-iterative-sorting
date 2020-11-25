# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    arrLen = len(arr)
    
    index = 0
    while index < arrLen - 1:
        num1 = arr[index]
        
        search_index = index + 1
        while search_index < arrLen:
            num2 = arr[search_index]
            if num2 < num1:
                num1 += num2
                num2 = num1 - num2
                num1 -= num2
                arr[index] = num1
                arr[search_index] = num2
            search_index += 1
        index += 1
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    arr_len = len(arr)

    index1 = 0
    while index1 < arr_len - 1:
        index2 = 0
        while index2 < arr_len - index1 - 1:
            current_num = arr[index2]
            next_num = arr[index2 + 1]
            if current_num > next_num:
                # swap
                arr[index2] += arr[index2 + 1]
                arr[index2 + 1] = arr[index2] - arr[index2 + 1]
                arr[index2] -= arr[index2 + 1]
            index2 += 1
        index1 += 1
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    if arr == []:
        return []
    # Get min and max
    maxValue = int(max(arr))
    minValue = int(min(arr))
    range_of_elements = maxValue - minValue + 1
    arrLen = len(arr)

    # Create a sieve-like array and output array
    count_arr = [0] * range_of_elements
    output_arr = [0] * arrLen

#    # Store count of each character
    index = 0
    while index < arrLen:
        elementPosition = arr[index] - minValue
        count_arr[elementPosition] += 1
        index += 1

    # Loop through count array so that count_arr[i] "now contains actial position of this element in output array
    index = 1
    while index < len(count_arr):
        count_arr[index] += count_arr[index - 1]
        index += 1

    # Build the output array
    index = arrLen - 1
    while index >= 0:
        count_arr_index = arr[index] - minValue
        count_arr_value = count_arr[count_arr_index]
        output_arr_index = count_arr_value - 1
        output_arr[output_arr_index] = arr[index]
        count_arr[arr[index] - minValue] -= 1
        index -= 1

    return output_arr

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    new_list = arrA + arrB
    for i in range(elements):
        mini = min(new_list)
        merged_arr[i] = mini
        new_list.remove(mini)

    print(merged_arr)
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    # need to split in half in half in half until
    head = 0
    tail = len(arr)-1
    mid = (head+tail)//2

    return arr
# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

merge([3, 10, 4], [9, 2, 19])
merge_sort([1, 45, 3, 2, 56, 23])

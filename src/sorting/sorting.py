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
    # results = []
    # i = 0
    # j = 0
    # while i < len(arrA) and j < len(arrB):
    #     if arrA[i] < arrB[j]:
    #         results.append(arrA[i])
    #         i += 1
    #     else:
    #         results.append(arrB[j])
    #         j += 1
    # while i < len(arrA):
    #     results.append(arrA[i])
    #     i += 1
    # while j < len(arrB):
    #     results.append(arrB[j])
    #     j += 1
    # return results


# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    #     # Your code here
    #     # need to split in half in half in half until
    if len(arr) <= 1:
        return arr
    mid = round(len(arr)//2)
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

#     return arr
# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

merge([3, 4, 5, 10], [2, 9, 19])
# merge_sort([1, 45, 3, 2, 56, 23])

# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    if end >= start:
        mid = (start + end)//2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
        if arr[mid] <= target:
            return binary_search(arr, target, mid + 1, end)
    else:
        return -1
    # STRETCH: implement an order-agnostic binary search
    # This version of binary search should correctly find
    # the target regardless of whether the input array is
    # sorted in ascending order or in descending order
    # You can implement this function either recursively
    # or iteratively


def agnostic_binary_search(arr, target):
    # Your code here

    if arr[0] < arr[len(arr)-1]:
        low = 0
        high = len(arr)-1
        print("running")
        while high >= low:
            mid = (low + high)//2
            if arr[mid] == target:
                return mid
            if arr[mid] > target:
                high = mid - 1
                # return agnostic_binary_search(arr, target)
            if arr[mid] <= target:
                low = mid + 1
                # return agnostic_binary_search(arr, target)

        else:
            return -1

    else:
        print("descending")
        high = 0
        low = len(arr)-1
        while low >= high:
            mid = (low + high)//2
            if arr[mid] == target:
                return mid
            if arr[mid] >= target:
                high = mid + 1
            if arr[mid] < target:
                low = mid - 1

        else:
            return -1

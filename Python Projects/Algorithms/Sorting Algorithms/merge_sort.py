import random
## Python uses Timsort which is derived from merge sort and insertion sort ##

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right= arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a,b,arr):
    i=j=k=0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1
    


if __name__ == '__main__':
    cases = [[10,5,2,7,34,2,7,8,9], [], [6], [9,8,7,6], [1,2,3,4,5]]

    for arr in cases:
       merge_sort(arr)
       print(arr)


# Testing for index
# arr_test = [0,1,2,3,4,5,6,7,8]
# mid_test = len(arr_test)//2
# left_test = arr[:mid_test]
# right_test = arr[mid_test:]

# print(mid_test)
# print(left_test)
# print(right_test)
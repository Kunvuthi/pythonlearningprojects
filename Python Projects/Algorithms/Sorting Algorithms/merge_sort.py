import math
import random


def MergeSort(arr):                 ## User Interface
    MergeSort2(arr, 0, len(arr)-1)  


def MergeSort2(arr, lb, ub):     
    if lb < ub:
        mid = math.floor((lb+ub)/2) 
        MergeSort2(arr, lb, mid)
        MergeSort2(arr, mid+1, ub)
        merge(arr, lb, mid, ub)

def merge(arr, lb, mid, ub):
    counter_left = lb
    counter_right = mid + 1
    counter_k = lb
    sublist = []

    while (counter_left <= mid) & (counter_right <= ub):  ## If both list's pointer are still pointing within the list
        if arr[counter_left] < arr[counter_right]: ## if left is smaller than right then the new sublist will append right
            sublist.append(arr[counter_left])
            counter_left += 1
        elif arr[counter_right] < arr[counter_left]: ## if right is smaller than left                                                    
            sublist.append(arr[counter_right]) ##       then the new sublist will append right
            counter_right += 1
        counter_k += 1
    if counter_left > mid: ## If left pointer is out of the left array
        while counter_right <= ub:         ## Loop all the left over stuff from the right array 
            sublist.append(arr[counter_right])
            counter_right += 1
            counter_k += 1
    elif counter_right > mid:
        while counter_left <= mid:           ## Vise Versa
            sublist.append(arr[counter_left])
            counter_left += 1
            counter_k += 1
    i = lb                         ## Update values in original array
    for val in sublist:
        arr[i] = val
        i += 1

arr = []
for i in range(15):
    arr.append(random.randint(0,51))


print(arr)
MergeSort(arr)
print(arr)
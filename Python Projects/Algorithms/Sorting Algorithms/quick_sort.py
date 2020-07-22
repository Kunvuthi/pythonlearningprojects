import math
import random

## Not working!


def partition(arr, low, high):
    pivot = getPivot(arr,low,high)
    pivotValue = arr[pivot]
    arr[low], arr[pivot] = arr[pivot], arr[low]
    pivot = low
    i = low 

    for z in range(low, high):
        if arr[z] <= pivotValue:            
            arr[i], arr[z] = arr[z], arr[i]
            i += 1
    arr[i], arr[pivot] = arr[pivot], arr[i]   
    return i


def QuickSort(arr):
    QuickSort2(arr, 0, len(arr)-1)


def getPivot(arr, low, high):
    mid = math.ceil((low + high) / 2)
    pivot = high 
    if (arr[low] < arr[mid]) & (arr[mid] < arr[high]):
        pivot = mid 
    elif arr[low] < arr[high]:
        pivot = low
    return pivot


def QuickSort2(arr, low, high):
    if low < high:

        part_index = partition(arr, low, high)

        QuickSort2(arr, low, part_index-1 )
        QuickSort2(arr, part_index+1, high) 




arr = []
for i in range(11):
    A = random.randint(0,51)
    arr.append(A)

print(arr)
QuickSort(arr)
print(arr)
print(len(arr))

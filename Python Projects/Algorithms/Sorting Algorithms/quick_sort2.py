import random as rd

def partition(arr, low, high):
    border = low - 1
    pivot = arr[high]

    for z in range(low,high):
        if arr[z] < pivot:
            border += 1
            arr[z], arr[border] = arr[border], arr[z] 
    arr[border + 1], arr[high] = arr[high], arr[border + 1]
    return (border + 1)

def quickSort(arr):
    quickSort2(arr, 0, len(arr)-1)

def quickSort2(arr, low, high):
    if low < high:

        part_index = partition(arr, low, high)

        quickSort2(arr, low, part_index-1)
        quickSort2(arr, part_index+1, high)

arr = []
for i in range(1000):
    A = rd.randint(0,1000)
    arr.append(A)

print(arr)
quickSort(arr)
print(arr)


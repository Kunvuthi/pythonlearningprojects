def selectionSort(arr):
    for i in range(len(arr)):
        index_compare = i
        for z in range(i+1, len(arr)):
            if (arr[z] < arr[index_compare]) & (arr[z] < arr[i]):
                index_compare = z
        arr[i], arr[index_compare] = arr[index_compare], arr[i]


arr = [9,4,2,1,6,5,3,10]
selectionSort(arr)
print(arr)
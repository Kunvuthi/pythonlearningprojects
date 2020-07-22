## This is a very easy to implement sorting algorithm which is not as efficient as other such as Merge Sort ##
## O(n^2) ##

def insertionSort(arr):

    for i in range(1,len(arr)):
        temp = arr[i]
        j = i - 1
        while (j >= 0) & (arr[j] > temp):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp 

arr = [2,6,3,8,3,1,10]
insertionSort(arr)
print(arr)




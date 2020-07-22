import random

## Before looking at the code, please understand what does Bubble Sort algorithm do. ##
## Note: It is simply placing the biggest number at the end of the list but iterating at n-1 of sequence.  ##
## Example: First loop: [5,2,6,1] ----> [2,5,6,1] ------> [2,5,6,1]-------> [2,5,1,6] End of first loop   ##
##          Second Loop: [2,5,1,6] ------> [2,1,5,6]-------> [2,1,5,6]                End of second loop ##
##          Third loop: [1,2,5,6] -------> [1,2,5,6]                                  End of third loop ##
## Not the best algorithm, it has a running time of O(n^2)                                             ##
## 1 + 2 + 3 + 4 + 5 + ..... + (n-1) Computational time will result in a sum calculed as sigma        ##


def BubbleSort(arr):
    for i in range(len(arr)-1): 
        for z in range(len(arr)-i-1):
            if arr[z] > arr[z+1]:
                index1 = arr[z]
                index2 = arr[z+1]
                arr[z], arr[z+1] = index2, index1
    return arr

## Random Numbers in List Generator
arr = []
for i in range(0,10):
    A = random.randint(0,51)
    arr.append(A)

print("Unsorted List: ", arr)
print("Sorted List: ", BubbleSort(arr))

import random
import time


startTime = 0
numbers = [random.randint(1,100) for i in range(10)]
print("Original list: " + str(numbers))

#Bubble sort
def bubbleSort(arr):
    b = arr.copy()
    swap = 0
    for i in range(len(b)):
        for j in range(len(b) - i - 1):
            if b[j] > b[j+1]:
                b[j] , b[j+1] = b[j+1] , b[j]
                swap += 1
    return b, swap

#Insertion sort
def insertionSort(arr):
    j = arr.copy()
    shift = 0
    for i in range(1,len(j)):
        key = j[i]
        k = i - 1

        while k >= 0 and j[k] > key:
            j[k+1] = j[k]
            shift += 1
            k -= 1
        key = j[k+1]
    return j, shift

#Merge sort
def mergeSort(arr):
    """if len(arr) <= 1:
        return arr"""
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
        
    result.extend(left or right)
    return result



#Execution
startTime = time.time()
b, swap = bubbleSort(numbers)
print("\nBubble sort: " + str(b))
print("Swaps: " + str(swap))
print("Time: " + str(time.time() - startTime))

startTime = time.time()
j, shift = insertionSort(numbers)
print("\nInsertion sort: " + str(j))
print("Swaps: " + str(shift))
print("Time: " + str(time.time() - startTime))

startTime = time.time()
m = mergeSort(numbers)
print("\nMerge sort: " + str(m))
print("Time: " + str(time.time() - startTime))
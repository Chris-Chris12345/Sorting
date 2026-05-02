#In merge sort, we divide the entire list into two halves. Sort each half first and then merge them.
#[8,3,6,4]
#[8,3] [6,4] --> [3,8] [4,6]
#3 vs 4 and 3 vs 6 => 3 is at the right place
#8 vs 4 and 8 vs 6 => 8 is greater then both 4 and 6
#[3,4,6,8]

#Merge sort works with large data sets
#Divide and conquer approach
#Time complexity = O(n log n)

def Merge(arr,low,mid,high):
    lis = []
    start1 = low
    start2 = mid + 1
    while start1 <= mid and start2 <= high:
        if arr[start1] < arr[start2]:
            lis.append(arr[start1])
            start1 += 1
        else:
            lis.append(arr[start2])
            start2 += 1

    while start1 <= mid:
        lis.append(arr[start1])
        start1 += 1

    while start2 <= high:
        lis.append(arr[start2])
        start2 += 1

    k = 0
    for i in range(low,high + 1):
        arr[i] = lis[k]
        k = k + 1
    
def MergeSort(arr,low,high):
    if low < high:
        mid = (low + high) // 2
        MergeSort(arr,low,mid)#First half/partition
        MergeSort(arr,mid + 1,high)#Second half/partition
        Merge(arr,low,mid,high)#Combining the 2 halves

arr = [3,7,8,1,6,4,9,2]
n = len(arr)
MergeSort(arr,0,n-1)
print(arr)
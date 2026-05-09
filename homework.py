def Merge(arr, low, mid, high):
    lis = []
    start1 = low
    start2 = mid + 1

    while start1 <= mid and start2 <= high:
        if arr[start1] > arr[start2]:
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
    for i in range(low, high + 1):
        arr[i] = lis[k]
        k += 1


def MergeSort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        MergeSort(arr, low, mid)
        MergeSort(arr, mid + 1, high)
        Merge(arr, low, mid, high)


scores = [72, 88, 95, 60, 83, 91]
n = len(scores)
MergeSort(scores, 0, n - 1)

print("Scores from highest to lowest:", scores)

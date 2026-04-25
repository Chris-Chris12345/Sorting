#Sorting is arraging the data in a particular order: ascending or descending
#Sorting makes the entire process faster. Exemple: Binary search works better then Linear search

#Ascending
aslis = [4,2,9,7,3]
aslis.sort()
print(aslis)

#Descending
desLis = [2,0,8,4,9]
desLis.sort(reverse=True)
print(desLis)

#Bubble sort: compares adjacent elements and swap them if they are in wrong order. Repeat until sorted
#[3,1,8,2]
#pass 1: [1,3,2,8]
#pass 2: [1,2,3,8]

lis = [3,7,1,8,0]
for i in range(0,len(lis)):
    for g in range(0,len(lis) - i - 1):
        if lis[g] > lis[g+1]:
            lis[g] , lis[g+1] = lis[g+1] , lis[g]

print(lis)

#Insertion sort: takes one element at a time, places it at its place in the sorted part exactly like how we arrange a deck of cards
#[4,1,8,0]
#[4] is at the correct place
#[1] will be placed before [4]: [1,4]
#[8] is at the correct place: [1,4,8]
#[0] will be placed before [1]: [0,1,4,8]

def InsertionSort(arr):
    for i in range(1,len(arr)):
        targ = arr[i]
        j = i-1

        while j >= 0 and arr[j] > targ:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = targ
    return arr

print(InsertionSort([5,2,9,4,1]))
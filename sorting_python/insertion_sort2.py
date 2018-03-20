def insertionSort(arr):
    for i in range(0, len(arr)):
        curIndex = arr[i]
        k=0
        for j in range(i-1, -2, -1):
            k=j
            if arr[j] > curIndex:
                arr[j+1] = arr[j]
            else:
                break
        arr[k+1]=curIndex
    return arr

# def insertion_sort2(arr):
#     for i in range(1, len(arr)):
#         j = i-1
#         while arr[j] > arr[j+1] and j >= 0:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#             j -= 1
#     return arr

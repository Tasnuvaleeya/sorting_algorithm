def selectionSort(arr):
    for i in range(0, len(arr)-1):
        minIndex = i
        # print( 'i =',minIndex)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
                # print( 'j =', minIndex)
        if minIndex != i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for arr_i in range(n):
        arr_t = str(input())
        print(arr_t)
        print(type(arr_t))

        arr.append(int(arr_t))
    result = selectionSort(arr)
    print("\n".join(map(str, result)))
    # print(result)

# print(selectionSort([31415926535897932384626433832795, 1, 3, 10, 3, 5]))




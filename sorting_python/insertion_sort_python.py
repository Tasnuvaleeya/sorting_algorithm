def insertion_sort(A):
    for i in range(1, len(A)):
        curNum = A[i]
        k=0

        for j in range(i-1, -2, -1):
            k=j
            if A[j] > curNum:
                A[j+1] = A[j]
            else:
                break
        A[k + 1] = curNum
    return A

print(insertion_sort([3, 4, 0, 2, 9, 3]))
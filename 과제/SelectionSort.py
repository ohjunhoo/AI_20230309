# 맨 뒷자리로 큰수를 이동시켜 정렬

def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def selectionsort2(A:list):
    for last in range(len(A)-1, 0, -1):
        k =theLargest(A,last)
        A[k], A[last] = A[last], A[k]
    return A

def theLargest(A:list, last):
    Largest = 0
    for i in range(last+1):
        if A[i] > A[Largest]:
            Largest = i
    return Largest
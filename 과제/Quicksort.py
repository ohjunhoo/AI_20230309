def quicksort(arr, p:int, r:int):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q-1)
        quicksort(arr, q+1, r)
    return arr


def partition(arr,p:int, r:int):
    x= arr[r]
    i = p-1
    for j in range(p,r):
        if arr[j] < x:
            i += 1
            arr[i], arr[j]= arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1


if __name__ == '__main__':
    unsorted = [3, 8, 2, 4, 8, 77, 1, 2, 0, 5, 56, 28]
    sorted_ = quicksort(unsorted, 0, len(unsorted)-1)
    print('---------------------------')
    print('Sorted Array', sorted_)
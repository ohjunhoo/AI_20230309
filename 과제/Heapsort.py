import Heap as hp

def heapSort(A):
    B = [x for x in A]
    h = hp.Heap(B)
    h.buildHeap()
    for i in range(len(B),0 -1):
        A[i] = h.deleteMax

def main():
    print("Heapsort!")
    # A = [3, 8, 2, 4, 8, 1, 2, 0, 5, 9]
    A = [3, 5, 1, 4, 2]
    print('A[]:       ', A)
    heapSort(A)
    print('Sorted A[]:', A)


if __name__ == '__main__':
    main()
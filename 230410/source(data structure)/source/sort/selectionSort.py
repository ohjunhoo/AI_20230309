def selectionSort(A):
	for last in range(len(A)-1, 0, -1):
		k = theLargest(A, last)	# A[0...last] 중 가장 큰 수 A[k] 찾기
		A[k], A[last] =  A[last], A[k]

def theLargest(A, last:int) -> int:	# A[0...last]에서 가장 큰 수의 인덱스를 리턴한다
	largest = 0
	for i in range(last+1):
		if A[i] > A[largest]:
			largest = i
	return largest

# 코드 9-1


def main():
    print("selectionSort test")
    A = [35, 24, 16, 21, 4, 72, 23, 9, 23, 14, 58, 12, 0]
    print("A[]:	   ", A)
    selectionSort(A)
    print("Sorted A[]:", A)

if __name__ == "__main__":
    main()

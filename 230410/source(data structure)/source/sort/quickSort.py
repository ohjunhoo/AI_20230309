def quickSort(A, p:int, r:int):
	if p < r:
		 q = partition(A, p, r)
		 quickSort(A, p, q-1)
		 quickSort(A, q+1, r)


def partition(A, p:int, r:int) -> int:
	x = A[r]					# x: 기준 원소
	i = p-1					# i: 1구역의 끝 지점
	for j in range(p, r):	# j: 3구역의 시작 지점
		if A[j] < x:
			i += 1
			A[i], A[j] = A[j], A[i]  # 교환
	
	A[i+1], A[r] = A[r], A[i+1]	   # 기준 원소와 2구역 첫 원소 교환
	print(f"Partitioning array from index {p} to {r}: {A}")
	print(f"Current pivot: {x}")
	print(f"Swapping {A[i+1]} and {A[r]}")
	print(f"Result: {A}\n")
	
	return i+1

# 코드 9-5


def main():
    print("Quicksort test")
    A = [3, 8, 2, 4, 8, 77, 1, 2, 0, 5, 56, 28]
    print("A[]:       ", A)
    quickSort(A, 0, len(A)-1)
    print("Sorted A[]:", A)
    
if __name__ == "__main__":
    main()

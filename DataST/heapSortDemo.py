from heap import Heap

def heapsort(x:list):
    buildHeap(x)
    for last in range(len(x)-1,0,-1):
        x[last], x[0] =x[0], x[last]
    percolateDown(x, 0, last-1)

def buildHeap(self):
		for i in range((len(self.__A) - 2) // 2, -1, -1):
			self.__percolateDown(i)
def percolateDown(self, i:int):
		# Percolate down w/ self.__A[i] as the root
		child = 2 * i + 1  # left child
		right = 2 * i + 2  # right child
		if (child <= len(self.__A)-1):
			if (right <= len(self.__A)-1 and self.__A[child] < self.__A[right]):
				child = right  # index of larger child
			if self.__A[i] < self.__A[child]:
				self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
				self.__percolateDown(child)   
def main():
    print("Heapsort")
    A= [3,8,2,4,8,1,2,0,5,9]
    print("A[]:     ",A)
    heapsort(A)
    print("Sorted A[]:",A)

if __name__ == "__main__":
    main()
    


    
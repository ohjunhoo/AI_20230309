class Heap:
    def __init__(self, *args):
        if len(args) != 0:
            self.__A =args[0]

        else:
            self.__A = []
# 구현: 힙에 원소 삽입하기(재귀 알고리즘)
    def insert(self, data):
        self.__A.append(data)
        self.__percolateup(len(self.__A)-1)
# 스며오르기
    def __percolateup(self, i:int):
        parent = i-1 // 2
        if i > 0 and self.__A[i] > self.__A[parent]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            self.__percolateup(parent)
# 구현: 힙에서 원소 삭제하기
    def deleteMax(self):
        if(not self.isEmpty()):
            max =self.__A[0]
            self.__A[0] =self.__A.pop() # pop() : 리스트의 끝 원소 삭제 후 원소 리턴
            self.__percolatedown(0)
            return max
        else:
            return None
# 스며내리기
    def __percolateDown(self,i:int):
        child = 2 * i + 1  # left child
        right = 2 * i + 2  # right child
        if(child <= len(self.__A)-1):
            if(right<=len(self.__A)-1 and self.__A[child] < self.__A[right]):
                child = right
        if self.__A[i] < self.__A[child]:
            self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
            self.__percolateDown(child)
    
    def max(self):
        return self.__A[0]

# 힙 만들기
    def buildHeap(self):
        for i in range((len(self.__A)-2) // 2, -1, -1):
            self.__percolateDown(i)

# 힙이 비었는지 확인하기
    def isEmpty(self) -> bool:
        return len(self.__A) == 0

    def clear(self):
        self.__A =[]

    def size(self):
        return len(self.__A)
        

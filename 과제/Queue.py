class Queue:
    def __init__(self):
        self.__queue=[]
    
    def enqueue(self,x):
        self.__queue.append(x)
    
    def dequeue(self):
        self.__queue.pop(0)
    
    def front(self):
        return self.__queue[0]
    
    def isEmpty(self) -> bool:
        return self.__queue.isEmpty()
    
    def dequeueAll(self):
        self.__queue.clear()
    
    def printQueue(self):
        print(self.__queue)

    def size(self):
        print(len(self.__queue))


q1 = Queue()
q1.enqueue("Mon")
q1.enqueue("Tue")
q1.enqueue(1234)
q1.enqueue("Wed")
q1.dequeue()
q1.enqueue('aaa')
q1.printQueue()
q1.dequeue()
q1.printQueue()
q1.dequeue()
q1.printQueue()
q1.dequeue()
q1.printQueue()
q1.size()
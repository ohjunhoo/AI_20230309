from listQueue import *

q1 = ListQueue()  #ListQueue class self.__init__(self)
q1.enqueue("Mon")
q1.enqueue("Tue")
q1.enqueue(1234)
q1.enqueue("Wed")
q1.dequeue()  # dequeue Mon
q1.enqueue('aaa')
q1.dequeue()  # dequeue Tue
q1.printQueue()

# 코드 7-7
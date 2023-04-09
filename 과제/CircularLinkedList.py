class ListNode:
    def __init__(self,newItem, next):
        self.item = newItem
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.__tail = ListNode("dummy",None)
        self.__tail.next  = self.__tail
        self.__numItems = 0

    def insert(self, i:int, newItem):
        if i >= 0 and i <= self.__numItems:
            prev = self.getNode(i-1)
            newNode = ListNode(newItem, prev.next)
            prev.next =newNode
            if i == self.__numItems:
                self.__tail = newNode
            self.__numItems +=1
        else:
            print(f"index,{i}: out of bound in inser()")
    
    def append(self,newItem):
        newNode = ListNode(newItem,  self.__tail.next)
        self.__tail =newNode
        self.__numItems +=1
    
    def pop(self, *args):
    # 가변 파라미터. 인자가 없거나 -1이면 마지막 원소로 처리하기 위함.
        if self.isEmpty():
            return None
        if len(args) != 0:
            i = args[0]
        
        if i > 0 and i <= self.__numItems-1:
            prev = self.getNode(i-1)
            retItem =prev.next.item
            prev.next =prev.next.next
        if i == self.__numItems-1:
            self.__tail = prev
            self.__numItems -=1
            return retItem
        else:
            return None
    def remove(self,x):
        (prev, curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next
        if curr == self.__tail:
            self.__tail = prev
            self.__numItems -=1
            return x
        else:
            return None
    
    def get(self, *args):
        if self.isEmpty():
            return None
        if len(args) == 0 or i == -1:
            i = self.__numItems -1
        if i > 0 and i <= self.__numItems -1:
            return self.getNode(i).item
        else:
            return None
    
    def index(self, x):
        cnt = 0
        for element in self:
            if element == x:
                return cnt
        cnt +=1
        return -12345

    def isEmpty(self):
        return self.__numItems == 0

    def size(self):
        return self.__numItems
    
    def clear(self):
        self.__tail = ListNode("dummy", None)
        self.__tail.next - self.__tail
        self.__numItems = 0
    
    def extend(self, a):
        for x in a:
            self.append(x)
    
    def copy(self):
        a = CircularLinkedList()
        for element in self:
            a.append(element)
        return a
    
    def reverse(self):
        __head = self.__tail.next
        prev = __head; curr = prev.next ; next=curr.next
        curr.next =__head; __head.next = self.__tail; self.__tail = curr
        for i in range(self.__numItems-1):
            prev = curr
            curr = next
            next = next.next
            curr.next= prev
    def sort(self):
        a =[]
        for element in self:
            a.append(element)
            a.sort()
            self.clear()
            for element in a:
                self.append(element)
    def __findNode(self, x):
        __head =prev= self.__tail.next
        curr = prev.next
        while curr != __head:
            if curr.item == x:
                return (prev, curr)
            else:
                prev = curr
                curr = curr.next
            return (None, None)
    def getNode(self, i:int):
        curr = self.__tail.next
        for index in range(i+1):
            curr  = curr.next
        return curr

    def printList(self):
        for element in self:
            print(element, end="")
            print()
    def __iter__(self):
        return CircularLinkedListIterator(self)

class CircularLinkedListIterator:
    def __init__(self, alist):
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next
    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else:
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
        return item

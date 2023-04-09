class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Linkedlist:
    
    def __init__(self,head=None):
        self.head = head
        self.count = 0

    def insert(self,i:int,data):
        if i >= 0 and i <= self.count:
            prev = self.getNode(i-1)
            node = Node(data, prev.next)
            prev.next = node
        self.count += 1
    
    def pop(self, i:int):
         if  i >= 0 and i <= self.count:
            prev = self.getNode(i-1)
            curr = prev.next
            prev.next = curr.next
            self.count -=1
            return curr.data
    
    def remove(self, data):
        (prev, curr) = self.findNode(data)
        if curr != None:
            prev.next = curr.next
            self.count -=1
            return data
        else:
            return None
    
    def append(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        self.count += 1

    def printlist(self):
        if self.head is None:
            print("EMPTY")
        else:
            curr = self.head
            while curr.next:
                print(curr.data, end="->")
                curr= curr.next
            if curr.next is None:
                    print(curr.data)
    
    def index(self, data):
        curr = self.head
        for index in range(self.count):
            if curr.data == data:
                return index
            else:
                curr = curr.next
        print("INDEX ERROR")
    
    def __isEmpty(self):
        return self.count == 0
    
    def size(self):
        return self.count
    
    def get(self, i:int):
        if self.__isEmpty():
            return None
        if (i >= 0 and i <= self.count):
            return self.getNode(i).data
        else:
            return None
    
    def getNode(self,i:int):
        curr = self.head
        for i in range(i):
            curr = curr.next
        return curr
    
    def findNode(self,data ):
        prev =self.head
        curr = prev.next
        while curr != None:
            if curr.data == x:
                return(prev,curr)
            else:
                prev = curr
                curr = curr.next
        return(None, None)
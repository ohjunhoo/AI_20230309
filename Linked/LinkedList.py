class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Linked_List(Node):
    
    def __init__(self):
        self.__head = Node("dummy")
        self.__numItems = 0 
    
    def insert(self, i:int,x):
         if i >= 0 and i <= self.__numItems:
             prev = self.__getNode(i-1)
             newNode = Node(x,prev.next)
             prev.next = newNode
             self.__numItems += 1
         else:
             print("index",i, ":out of bound in insert()")
    
    def append(self, data):
        prev = self.__getNode(self.__numItems-1)
        newNode  = Node(data, prev.next)
        prev.next =newNode
        self.__numItems += 1
    
    def pop(self, i:int):
        if i >= 0 and i <= self.__numItems-1:
            prev = self.__getNode(i-1)
            curr = prev.next
            prev.next = curr.next
            Item = curr.data
            self.__numItems -=1
            return Item
        else:
            return None
    def remove(self,x):
        (prev, curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next
            self.__numItems -=1
            return x
        else:
            return None
    def get(self, i:int):
        if self.isEmpty():
            return None
        if( i >= 0 and i <= self.__numItems -1):
            return self.__getNode(i).item
        else:
            return None
    
    def index(self,x):
        curr = self.head.next
        for index in range(self.__numItems):
            if curr.item == x:
                return index
            else:
                curr = curr.next
        return -12345
    
    def isEmpty(self):
        return self.__numItems == 0
    def size(self):
        return self.__numItems
    def clear(self):
        self.__head = Linked_List("dummy", None)
        self.__numItems = 0
    def count(self,x):
        cnt = 0
        curr = self.head.next
        while curr != None:
            if curr.item == x:
                cnt +=1 
            curr = curr.next
        return cnt
    
    def extend(self, a):
        for index in range(a.size()):
            self.append(a.get(index))
    
    def copy(self):
        a = Linked_List()
        for index in range(self.__numItems):
            a.append(self.get(index))
        return a 
    
    def reverse(self):
        a = Linked_List()
        for index in range(self.__numItems):
            a.insert(0, self.get(index))
        self.clear()
        for index in range(a.size()):
            self.append(a.get(index))
    
    def sort(self):
        a = []
        for index in range(self.__numItems):
            a.append(self.get(index))
        a.sort()
        for index in range(len(a)):
            self.append(a[index])
    def printList(self):
        curr = self.__head.next
        while curr != None:
            print(curr.item, end="")
            curr = curr.next
        print()
    def __findNode(self,x):
        prev = self.__head
        curr = prev.next
        while curr != None:
            if curr.item == x:
                return(prev,curr)
            else:
                prev = curr
                curr = curr.next
        return(None, None)
    
    def __getNode(self, i:int):
        curr = self.__head
        for i in range(i+1):
            curr = curr.next
        return curr

list = Linked_List()

list.append(30)
list.insert(0,20)
class ChainHashTable:
    bkbox = 7
    def __init__(self,n):
        self.table =[CircularLinkedList()for i in range(n)]
        self.count = 0
    def __hash(self,x:int):
        x % len(self.table)
    def insert(self, x:int):
        slot = self.__hash(x)
        self.table[slot].insert(0,x)
        self.count+=1
    def search(self, x:int):
        slot =self.__hash(x)
        if self.table[slot].isEmpty():
            return None
        else:
            head =prev =self.table[slot].getNode(-1)
            curr =prev.next
            while curr != head:
                if curr.item == x:
                    return curr
                else:
                    curr = curr.next
    def delete(self,x:int):
        pass
    def isEmpty(self):
        if len(self.count) ==0:
            print("EMPTY")
    def clear(self):
        self.table = None
        
        
        
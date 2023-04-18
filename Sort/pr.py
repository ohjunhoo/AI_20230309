class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Chain:
    def __init__(self):
        self.head = None
        self.count = 0

class HashTable:
    def __init__(self, n:int):
        self.table = [Chain() for i in range(n)]
        self.count = 0
    
    def hash(self,x:int):
        x % len(self.table)

    def insert(self, x:int, data):
        newNode = Node(data)
        slot = self.hash(x)
        
        if self.table[slot].head is None:
            self.table[slot] = newNode
        
        else:
            curr = self.table[slot]
            for i in range(self.count):
                curr = curr.next
            curr.next = newNode        
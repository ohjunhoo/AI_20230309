from LinkedList import Linked_List

class LinkedStack:
    def __init__(self):
        self.__list =Linked_List()
    
    def push(self,newItem):
        self.__list.insert(0,newItem)
    
    def pop(self):
        self.__list.pop(0)
        return self.__list.pop(0)
    
    def top(self):
        return self.__list.get(0) 
    
    def isEmpty(self) -> bool:
        return self.__list.isEmpty()
    
    def popAll(self):
        return self.__list.clear()
    
    def printStack(self):
        print("Stack from top:", end="")
        for i in range(self.__list.size()):
            print(self.__list.get(i), end="")
        print()    


st1 = LinkedStack()
st1.push(100)
st1.push(200)

print("Top is", st1.top())

st1.pop()
st1.push("Monday")
st1.printStack()
print("isEmpty?", st1.isEmpty())       


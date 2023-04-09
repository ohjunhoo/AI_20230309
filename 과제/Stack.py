class ListStack:
    
    def __init__(self):
        self.__stack=[]
        self.count = 0
    
    def push(self,data):
        self.__stack.append(data)
        self.count +=1
    
    def pop(self):
        self.__stack.pop()
        self.count -=1
    
    def top(self):
        if self.count == 0:
            return "EMPTY LIST"
        return self.__stack[-1]
    
    def isEmpty(self):
        if self.count == 0:
            return True
        return False
    
    def popAll(self):
        self.__stack.clear()
        self.count = 0
    
    def printStack(self):

        for i in range((self.count)):
            print(self.__stack[i])

if __name__ == '__main__':
    st1 = ListStack()
    print(st1.top())	# No effect
    st1.push(100)
    st1.push(200)
    print("Top is", st1.top())
    st1.pop()
    st1.push('Monday')
    st1.printStack()
    print('isEmpty?', st1.isEmpty())
    print(st1.top())
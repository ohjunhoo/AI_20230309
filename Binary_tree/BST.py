class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinartSearchTree:
    def __init__(self):
        self.root =None
        self.count = 0
    def search(self, x):
        curr = self.root
        for _ in range(self.count):
            if curr.data == x:
                print(curr.data)
                curr = curr.left
            if  curr.data == x:
                print(curr.data)
                curr =  curr.right
                
    def insert(self, newItem):
            # self.__arr.append(TreeNode(newItem))
            # for i in range(self.count):
            #     for j in range(i, self.count):
            #         if self.__arr[j] > self.__arr[j+1]:
            #             self.left = self.__arr[j+1]
            #         else:
            #             self.right = self.__arr[j+1]
            # self.count +=1
            newNode = TreeNode(newItem)
            if self.root is None:
                self.root = newNode
                self.count += 1 
            else:
                curr = self.root
                for _ in range(self.count):
                    if curr.data > newNode.data:
                        curr.left = newNode
                        curr = curr.left
                        self.count+=1
                    else:
                        curr.light =  newNode
                        curr = curr.right
                        self.count += 1    
    def delete(self):
        pass
    def isEmpty(self):
        pass
            

a = BinartSearchTree()
a.insert(10)
a.insert(20)
a.insert(30)
a.insert(40)

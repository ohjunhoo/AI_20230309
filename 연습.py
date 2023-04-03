#Write a Python program to search a specific item in a given WSU linked list 
#Then return true if the item is found otherwise return false.

#Class Node wich will generate Node for Linked List 
from typing import Dict


class Node(object):
    # Singly linked node which make you to step forward and step backward
    # Thus you need to link of data 
    # pre: 
    #     1) data will be class name as string
    #     2) corder: class priority for taking
    #     3) next : next of node
    #     4) prev : previous of node
    def __init__(self, data=None, classorder=None, next=None, prev=None):
        self.data = data
        self.corder = classorder
        self.next = next
        self.prev = prev
        
#WSU Linked List Class for finding the class which are taughted by WSU
#This Ojbect will contain the order of class
#If you want to find class order to take, then you should check the order
class WSU_linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    #pre: Node object which has data
    #Method: add data in the linked List
    #Output: Update Linked list of new class
    def append_item(self, data, classorder):
       # Append an item 
        new_item = Node(data, classorder, None, None)
        
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item
        self.count += 1
           
        
        #disconnect Link and setup new_item
        #check linked list if there are value that is looked by object   
    def iter(self):
        current = self.head
        while current:
            itemval = current.data
            current = current.next
            yield itemval
            
#define sorted class list
# precondition: node data with class list by append function
# method: sort class list in terms of class order 
# output: 
#        1) return  none 
#        2) print class list in priority of class order
    def sorted_classlist(self):
        node = self.head
        result=[]
        for _ in range(self.count):
            result.append(node.data)
            node = node.next
        return result

#print each elements
    def print_foward(self):
       for node in self.iter():
        print(node)


#search by end of linked list        
    def search_item(self, val):
       for node in self.iter():
            if val == node: 
                return True
       return False

#set Program Language Linked List for set Node
#The classes are in this order 
#Please set as this order 
#Now WS university decide the priority of class taking
#Please show class priority 
items = WSU_linked_list() #Instance linked List of Node Object
items.append_item('PHP', 5)  #input program language
items.append_item('Python', 1)
items.append_item('C#', 3)
items.append_item('C++', 2)
items.append_item('Java',4)
items.append_item('SQL',7)
items.append_item('Compiler',6)

print("Original list:")
items.print_foward()
print("\n")
print("You should take class as below order")
items.sorted_classlist()






'''
if items.search_item('SQL'):
    print("True")
else:
    print("False")

if items.search_item('C+'):
    print("True")
else:
    print("False")
'''

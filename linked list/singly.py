#node class(structure of each node)
class Node:
    def __init__(self,data):
        self.data=data #store the data from user
        self.next=None #pointer to next node

#linked list class
class Linkedlist:
    def __init__(self):
        self.head=None #initially empty list
    
    #traversing (display all elements)
    def traversal(self):
        if self.head is None:
            print("List is empty")
            return
        temp=self.head
        while temp:
            print(temp.data,end=" ->")
            temp=temp.next
        print("None")
    
    #searching (find element)
    def search(self,key):
        temp=self.head
        pos=1
        while temp:
            if temp.data==key:
                print("Element found at position: ",pos)
                return
            temp=temp.next
            pos+=1
        print("Element is not found....")
    
    #insertion at beginning
    def insert_beg(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    #insert at end
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    #insert at any position (vvi)
    def insert_pos(self,data,pos):
        new_node=Node(data)
        if pos==1:
            new_node.next=self.head
            self.head=new_node
            return
        temp=self.head
        for i in range(pos-2):
            if temp is None:
                print("Invalid Position...")
                return
            temp=temp.next
        
        new_node.next=temp.next
        temp.next=new_node
    #deletion from beg
    def delete_beg(self):
        if self.head is None:
            print("List is empty: ")
            return
        self.head=self.head.next
    #delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty: ")
            return
        if self.head.next is None:
            self.head=None
            return
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
    #deletion by value
    def delete_value(self,key):
        if self.head is None:
            print("List is empty")
            return
        #if first node to delete
        if self.head.data==key:
            self.head=self.head.next
            return
        #other than first
        temp=self.head
        while temp.next:
            if temp.next.data==key:
                temp.next=temp.next.next
                return 
            temp=temp.next
        print("Element not found")

l1=Linkedlist()
l1.insert_beg(10)
l1.insert_beg(5)
l1.insert_end(30)
l1.insert_end(50)
l1.insert_beg(20)
l1.insert_beg(50)

print("Linked lis: ")
l1.traversal()
l1.search(50)

l1.insert_pos(15,3) #data,position
print("After insertion at position: ")
l1.traversal()

l1.delete_beg()
print("After deletion at begg: ")
l1.traversal()

l1.delete_end()
print("After deletion at end: ")
l1.traversal()

l1.delete_value(30)
print("After deleting value 30: ")
l1.traversal()
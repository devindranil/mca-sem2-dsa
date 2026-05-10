# Python Program to Implement Doubly Linked List

# Node class represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data      # Store data
        self.prev = None      # Pointer to previous node
        self.next = None      # Pointer to next node


# Doubly Linked List class
class DoublyLinkedList:

    # Constructor to initialize head pointer
    def __init__(self):
        self.head = None


    # Insert a node at the beginning
    def insert_at_beginning(self, data):

        # Create a new node
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Link new node with current head
        new_node.next = self.head
        self.head.prev = new_node

        # Move head to new node
        self.head = new_node


    # Insert a node at the end
    def insert_at_end(self, data):

        # Create a new node
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        temp = self.head
        while temp.next:
            temp = temp.next

        # Connect last node with new node
        temp.next = new_node
        new_node.prev = temp


    # Delete a node by value
    def delete_node(self, key):

        # If list is empty
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        # If head node itself contains the key
        if temp.data == key:

            # Move head to next node
            self.head = temp.next

            # Make previous of new head None
            if self.head:
                self.head.prev = None

            return

        # Search for the node to delete
        while temp and temp.data != key:
            temp = temp.next

        # If key not found
        if temp is None:
            print("Node not found")
            return

        # Connect previous node with next node
        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next


    # Display the list in forward direction
    def display_forward(self):

        # If list is empty
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        print("Forward Traversal:")

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


    # Display the list in reverse direction
    def display_reverse(self):

        # If list is empty
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        # Move to last node
        while temp.next:
            temp = temp.next

        print("Reverse Traversal:")

        # Traverse backward
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


# Driver Code

# Create Doubly Linked List object
dll = DoublyLinkedList()

# Insert elements
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_end(30)
dll.insert_at_end(40)

# Display list
dll.display_forward()

# Display reverse traversal
dll.display_reverse()

# Delete a node
dll.delete_node(30)

# Display list after deletion
print("\nAfter Deleting 30:")
dll.display_forward()
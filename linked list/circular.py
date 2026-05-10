# Python Program to Implement Circular Linked List

# Node class
class Node:
    def __init__(self, data):
        self.data = data      # Store data
        self.next = None      # Pointer to next node


# Circular Linked List class
class CircularLinkedList:

    # Constructor
    def __init__(self):
        self.head = None


    # Insert node at the end
    def insert(self, data):

        # Create new node
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            new_node.next = self.head   # Point to itself
            return

        # Traverse to the last node
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        # Connect last node to new node
        temp.next = new_node

        # New node points to head
        new_node.next = self.head


    # Display Circular Linked List
    def display(self):

        # If list is empty
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        print("Circular Linked List:")

        # Traverse until reaching head again
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(Back to Head)")


    # Delete a node by value
    def delete(self, key):

        # If list is empty
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        prev = None

        # If head node contains the key
        if current.data == key:

            # Single node case
            if current.next == self.head:
                self.head = None
                return

            # Find last node
            last = self.head
            while last.next != self.head:
                last = last.next

            # Move head
            self.head = current.next

            # Last node points to new head
            last.next = self.head
            return

        # Search for node
        while current.next != self.head:
            prev = current
            current = current.next

            if current.data == key:
                break

        # If node found
        if current.data == key:
            prev.next = current.next
        else:
            print("Node not found")


# Driver Code

# Create Circular Linked List
cll = CircularLinkedList()

# Insert elements
cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.insert(40)

# Display list
cll.display()

# Delete a node
cll.delete(30)

# Display after deletion
print("\nAfter deleting 30:")
cll.display()
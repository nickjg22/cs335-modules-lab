class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_head(self, data) -> None:
        
        """Implement O(1) insertion at head"""
        new_node = Node(data)
        
        # Scenario 1: The list is currently empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # Scenario 2: The list already has elements
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
        self.size += 1

    def remove_from_tail(self):
        
        """Implement O(1) removal from tail (returns the data)"""
        # Scenario 1: List is empty
        if self.tail is None:
            return None
            
        data_to_return = self.tail.data
        
        # Scenario 2: Only one node in the list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # Scenario 3: Multiple nodes in the list
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            
        self.size -= 1
        return data_to_return

    def search(self, key_condition_func) -> Node:
        
        """Linear search O(n) using a lambda/condition function"""
        current = self.head
        
        # Traverse from head to tail
        while current is not None:
            # key_condition_func expects a node's data payload and returns True/False
            if key_condition_func(current.data):
                return current
            current = current.next
            
        return None  # Return None if no match is found
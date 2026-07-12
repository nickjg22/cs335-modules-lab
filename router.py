from structures.static_array import StaticArray
from structures.dynamic_linked_list import DoublyLinkedList

class TelemetryBufferQueue:
    """
    Behavior Requirement: FIFO (First In, First Out)
    Constraint: Data volume fluctuates intensely. 
    Selection: Should we use a Static Array or a Dynamic Linked List?
    """
    def __init__(self):
        # Instantiated with the dynamic structure to handle variable bursts
        self.storage = DoublyLinkedList() 

    def enqueue_packet(self, packet: dict) -> None:
        """Add a packet to the queue (Insert at the Head)"""
        self.storage.insert_at_head(packet)

    def dequeue_packet(self) -> dict:
        """Remove and return the oldest packet (Remove from the Tail)"""
        # If queue is empty, remove_from_tail returns None
        return self.storage.remove_from_tail()


class EmergencyOverrideStack:
    """
    Behavior Requirement: LIFO (Last In, First Out)
    Constraint: Memory is strictly limited to 10 slots for system stability.
    Selection: Array-based stack vs Linked List stack? 
    """
    def __init__(self, max_capacity=10):
        # Instantiated with a fixed size to respect memory limits
        self.storage = StaticArray(max_capacity)
        self.max_capacity = max_capacity
        self.top_index = -1

    def push_critical_signal(self, error_code: str) -> None:
        """Push onto stack. Raise OverflowError if max_capacity exceeded."""
        if self.top_index >= self.max_capacity - 1:
            raise OverflowError("Emergency stack is full! Cannot push critical signal.")
        
        self.top_index += 1
        # Change bracket assignment to explicit .set() method
        self.storage.set(self.top_index, error_code)

    def pop_critical_signal(self) -> str:
        """Pop from stack. Raise IndexError if empty."""
        if self.top_index == -1:
            raise IndexError("Emergency stack is empty! No critical signals to pop.")
        
        # Change bracket retrieval to explicit .get() method
        error_code = self.storage.get(self.top_index)
        self.top_index -= 1
        return error_code

class GridZoneNode:
    """
    Behavior Requirement: Hierarchical / Non-Linear Tree Organization
    """
    def __init__(self, zone_name: str):
        self.zone_name = zone_name
        self.children = [] # Holds sub-zone nodes

    def add_sub_zone(self, child_node) -> None:
        self.children.append(child_node)

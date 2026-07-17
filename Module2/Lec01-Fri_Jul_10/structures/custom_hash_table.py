from structures.dynamic_linked_list import DoublyLinkedList

class KeyValuePair:
    def __init__(self, key: str, value: any):
        self.key = key
        self.value = value

class SensorRegistryHashTable:
    """
    A fixed-bucket Hash Table using Chaining for collision resolution.
    Forces students to understand how a Hash Table optimizes access time 
    under fixed memory constraints.
    """
    def __init__(self, num_buckets: int = 10):
        self.num_buckets = num_buckets
        # An array of Dynamic Linked Lists to handle collisions
        self.buckets = [DoublyLinkedList() for _ in range(num_buckets)]

    def _hash_function(self, key: str) -> int:
        """Simple deterministic hash function to map key to an index."""
        return sum(ord(char) for char in key) % self.num_buckets

    def put(self, key: str, value: any) -> None:
        """
        1. Compute the bucket index using self._hash_function(key).
        2. Search the DoublyLinkedList at that bucket to see if the key already exists.
        3. If the key exists, update its value.
        4. If it doesn't exist, insert a new KeyValuePair at the head of the linked list.
        """
        # 1. Compute bucket index
        bucket_index = self._hash_function(key)
        linked_list = self.buckets[bucket_index]
        
        # 2. Search for the key using our custom search function
        existing_node = linked_list.search(lambda pair: pair.key == key)
        
        # 3. If key exists, update its value
        if existing_node is not None:
            existing_node.data.value = value
        # 4. If it doesn't exist, insert a new pair at the head
        else:
            new_pair = KeyValuePair(key, value)
            linked_list.insert_at_head(new_pair)

    def get(self, key: str) -> any:
        """
        1. Compute the bucket index.
        2. Search the linked list at that bucket for the key.
        3. Return the value if found, otherwise raise KeyError.
        """
        # 1. Compute bucket index
        bucket_index = self._hash_function(key)
        linked_list = self.buckets[bucket_index]
        
        # 2. Search for the key
        matching_node = linked_list.search(lambda pair: pair.key == key)
        
        # 3. Return value or raise KeyError
        if matching_node is not None:
            return matching_node.data.value
        
        raise KeyError(f"Key '{key}' not found in the registry.")

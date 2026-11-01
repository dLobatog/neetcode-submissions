class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # stores pointer to LL node
        self.head = Node() # .next is LRU
        self.tail = Node() # .prev is MRU
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.remove(self.cache[key])
        self.insert_right(self.cache[key])
        return self.cache[key].val
       
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert_right(node)
            return

        if len(self.cache) == self.capacity:
            # remove before adding
            lru = self.head.next 
            self.remove(self.head.next)
            del self.cache[lru.key]

        node = Node(key, value)
        self.insert_right(node)
        self.cache[key] = node
      

    def remove(self, node: Node) -> None:
        # node_prev <-> node <-> node_next
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next # prev -> next
        node_next.prev = node_prev # prev <- next 

      

    def insert_right(self, node: Node) -> None:
        # orig_prev -> tail
        orig_prev = self.tail.prev 
        # orig_prev <-> node <-> self.tail
        orig_prev.next = node # prev -> node
        node.prev = orig_prev # prev <- node
        self.tail.prev = node # node <- tail
        node.next = self.tail # node -> tail 

      
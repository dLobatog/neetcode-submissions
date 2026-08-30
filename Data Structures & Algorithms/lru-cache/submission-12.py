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
            self.remove(self.cache[key])

        self.cache[key] = Node(key=key, val=value)
        self.insert_right(self.cache[key])

        while len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

    def remove(self, node: Node) -> None:
        nxt, prev = node.next, node.prev
        # make previous node point to next
        # prev <-> node <-> next
        node.prev.next = nxt
        # prev <- node <-> next | prev -> next
        # make next node point to previous
        node.next.prev = prev
        # prev <- node -> next | prev <-> next
        # node disapears and will be GC

    def insert_right(self, node: Node) -> None:
        # insert at right.prev
        node_to_left = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        # now, we have node_to_left | node <-> tail
        node.prev = node_to_left
        node_to_left.next = node
        # now, we have node_to_left <-> node <-> tail

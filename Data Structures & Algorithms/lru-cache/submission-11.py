class Node:
    def __init__(self, key=None, val=None, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}
        # Left = LRU, Right = MRU
        self.right = Node()
        self.left = Node()
        self.left.next, self.right.prev = self.right, self.left
        

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        

    # insert_at_right
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = node
        self.right.prev = node
        node.prev = prv
        node.next = nxt
        

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1

        # update the list by putting this at the right ends
        self.remove(self.keys[key])
        self.insert(self.keys[key])
        #. -------
        # print('g', self.keys)
        return self.keys[key].val
        
    
    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.remove(self.keys[key])
        
        self.keys[key] = Node(key=key, val=value)
        # now insert at the end,as it's MRU
        self.insert(self.keys[key])
        # print('p', self.keys)

        while len(self.keys) > self.capacity:
            lru = self.left.next 
            self.remove(lru) 
            del self.keys[lru.key]
            
        
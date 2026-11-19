class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class MyHashSet:
    def __init__(self):
        self.indices = [None] * 1000000
        

    def add(self, key: int) -> None:
        idx = key % len(self.indices)

        if self.indices[idx] is None:
            self.indices[key % len(self.indices)] = Node(key)
            return 
        
        node = self.indices[idx]
        if node.key == key:
            return 
        # open addressing, add to end of list
        while node.next:
            node = node.next
            if node.key == key:
                return
        # no node found with this key? append
        new_node = Node(key)
        node.next = new_node
        new_node.prev = node


    def remove(self, key: int) -> None:
        idx = key % len(self.indices)

        if self.indices[idx] is None:
            return 
        
        node = self.indices[idx]
        if node.key == key:
            # delete this node by substituting with next node (or None)
            if node.prev:
                node.prev.next = node.next
            else:
                self.indices[idx] = node.next

            if node.next:
                node.next.prev = node.prev
            return 

        # open addressing, see if it's at end of list
        while node.next:
            node = node.next
            if node.key == key:
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.indices[idx] = node.next

                if node.next:
                    node.next.prev = node.prev
                return 


        # not found in that space? return
        return

    def contains(self, key: int) -> bool:
        idx = key % len(self.indices)
        if self.indices[idx] is None:
            return False

        node = self.indices[idx]
        while node and node.key != key:
            node = node.next

        if node and node.key == key:
            return True
        return False
        
            

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
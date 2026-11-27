class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val

class MyCircularQueue:

    def __init__(self, k: int):
        self.head_dummy = Node(None)
        self.tail_dummy = Node(None)
        self.head_dummy.next = self.tail_dummy
        self.head_dummy.prev = self.tail_dummy
        self.tail_dummy.next = self.head_dummy
        self.tail_dummy.prev = self.head_dummy
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.size >= self.capacity:
            return False
        
        cur = self.tail_dummy # find first available spot
        new_node = Node(value)
        # orig_prev <-> new_node <-> tail_dummy
        orig_prev = cur.prev
        cur.prev = new_node
        new_node.next = cur
        new_node.prev = orig_prev
        orig_prev.next = new_node
        self.size += 1
        return True
        

    def deQueue(self) -> bool:
        # find first element from tail and pop it
        if self.size == 0:
            return False

        node = self.head_dummy.next
        orig_next = node.next
        self.head_dummy.next = orig_next
        # print(node.val, node.next, node.prev)
        orig_next.prev = self.head_dummy
        self.size -= 1
        return True
        

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.head_dummy.next.val
        

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.tail_dummy.prev.val
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
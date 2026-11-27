class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val

class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [0] * k
        self.head = 0
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        tail = (self.head + self.size) % self.capacity
        self.arr[tail] = value # get the value at tail position
        self.size += 1
        return True
        

    def deQueue(self) -> bool:
        # find first element from tail and pop it
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True
        

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.arr[self.head]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.head + self.size - 1) % self.capacity]
        

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
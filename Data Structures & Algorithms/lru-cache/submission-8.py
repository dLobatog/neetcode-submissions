class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = OrderedDict()

    def get(self, key: int) -> int:
        # can return in o(1) with a hash
        if key not in self.keys:
            return -1
        # print('g', self.keys, self.q)
        # update the fact it was recently used, move to end
        # print('g', self.keys)
        self.keys.move_to_end(key, last=True)
        return self.keys[key]
        
    
    def put(self, key: int, value: int) -> None:
        self.keys[key] = value
        self.keys.move_to_end(key, last=True)
        # print(self.keys)
        while len(self.keys) > self.capacity:
            # remove LRU key if capacity exceeded
            self.keys.popitem(last=False)
            
class RandomizedSet:

    def __init__(self):
        self.values = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False

        self.values.append(val)
        self.index[val] = len(self.values)-1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False

        indexToRemove = self.index[val]
        if indexToRemove != len(self.values)-1: 
            self.values[-1], self.values[indexToRemove] = self.values[indexToRemove], self.values[-1]
            self.index[self.values[indexToRemove]] = indexToRemove
        self.values.pop()

        del self.index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
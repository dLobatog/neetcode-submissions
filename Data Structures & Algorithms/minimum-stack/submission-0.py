class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        if len(self.s) == 0:
            minval = val
            self.s.append((val, minval))
        else:
            minval = min(val, self.s[-1][1])
            self.s.append((val, minval))

    def pop(self) -> None:
        self.s = self.s[:-1]

    def top(self) -> int:
        return self.s[-1][0]
        
    def getMin(self) -> int:
        return self.s[-1][1]
        

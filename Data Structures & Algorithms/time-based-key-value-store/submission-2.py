class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((value, timestamp)) # since we know timestamps are set strictly increasing 
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.keys[key]
        # find timestamp_prev s.t timestamp_prev <= timestamp (maximize timestamp_prev)  
        l, r = 0, len(values)-1
        mid = (l + r)//2
        while l <= r:
            if values[mid][1] > timestamp:
                r = mid-1
            else:
                # move right because timestamp < value but we want the highest one
                l = mid + 1

            mid = (l + r)//2

        if mid >= 0 and mid < len(values) and values[mid][1] <= timestamp:
            return values[mid][0]
        else:
            return ""
        

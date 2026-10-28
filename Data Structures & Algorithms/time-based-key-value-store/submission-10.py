class TimeMap:
    # keys { "alice": [(happy, 1)] }
    # get alice 1
    # l=0, r=0 mid=0, value_ts == timestamp 1==1, returns happy
    # get alice 2
    # l=0, r=0, mid=0, value_ts > timestamp 2>1
    # r=-1 because we wanted to look in the left
    # ran out of space [0, -1]... why not return last value? 

    # keys { "key1": [(value1, 10)] }
    # get key1, 1
    # 1 >= timestamp1


    def __init__(self):
        self.keys = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((value, timestamp)) # since we know timestamps are set strictly increasing 
        
    def get(self, key: str, timestamp: int) -> str:
        # we can do bsearch on the key timestamps, and return either timestamp or previous
        values = self.keys[key]
        
        if len(values) == 0:
            return ""

        l, r = 0, len(values)-1
        while l <= r:
            mid = (l+r) // 2
            value, value_ts = values[mid]
            if value_ts > timestamp:
                # look on the left
                r = mid-1
            elif value_ts <= timestamp:
                # value is potentially ok, but is it the closest to timestamp?
                l = mid+1
        
        return values[r][0] if r >= 0 else ""
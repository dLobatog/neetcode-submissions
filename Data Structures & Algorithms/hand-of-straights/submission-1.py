class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # hand[i] = value
        # groupSize
        # each group is of size groupSize and card values consecutively increase by 1
        # [1 2 3 3 4
        count = Counter(hand)

        def buildGroup():
            # start
            cur = min(count.keys())
            # build
            # print(count)
            for i in range(groupSize):
                if cur in count:
                    count[cur] -= 1
                    if count[cur] == 0:
                        del count[cur]
                    cur += 1
                else:
                    return False
            return True

        # how many times to call buildGroup? until count 
        while len(count.keys()) != 0:
            if buildGroup() is False:
                return False

        return True
            
        





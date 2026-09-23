class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # hand[i] = value
        # groupSize
        # each group is of size groupSize and card values consecutively increase by 1
        # [1 2 3 3 4
        count = Counter(hand)

        for num in hand:
            # find earliest start from num:
            start = num
            while count[start - 1] > 0:
                start -= 1
    
            while count[start] > 0:
                for i in range(start, start+groupSize):
                    # print(i, count)
                    if i not in count or count[i] == 0:
                        return False
                    else:
                        count[i] -= 1
            

        return True
            
        





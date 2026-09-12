class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas at ith station
        # cost is ith to ith+1 station 
        # begin with 0 at one gas station
        # try to travel from gas station to another
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                # i didn't work
                total = 0
                res = i + 1 

        return res

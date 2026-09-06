class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            # no water can be trapped
            return 0

        i, j = 0, 1
        # monotonic non-decreasing stack from left to right
        #.  - to see rightmax
        # monotonic non-decreasing stack from right to left 
        #.  - to see leftmax

        leftMax = deque()
        rightMax = []

        for i, h in enumerate(height):
            if leftMax and h < leftMax[-1][1]: # - don't append,
                continue
            else: #- append
                leftMax.append((i, h))
            
        # [(0, 0), (1, 1), (3, 2), ...]
        # whenever we move later, we will need to popleft those items with i <= cur

        for i in range(len(height)-1, -1, -1):
            h = height[i]
            if rightMax and h < rightMax[-1][1]:
                continue
            else:
                rightMax.append((i, h))

        # at each position, we will use the proper leftMax, rightMax to compute
        total = 0 

        for i in range(len(height)):
            # popleft from both stacks first
            # Why inspect [1]? Because you are asking whether the next record is ready to replace the current one.
            while len(leftMax) > 1 and leftMax[1][0] <= i:
                leftMax.popleft()
            if rightMax and i > rightMax[-1][0]:
                rightMax.pop()

            # print(leftMax, rightMax, height[i])

            if leftMax and rightMax:
                # print("vals,", leftMax[0][1], rightMax[-1][-1], height[i])
                rain = min(leftMax[0][1], rightMax[-1][1]) - height[i] 
                if rain > 0:
                    # print("rain,", rain)
                    total += rain

        return total
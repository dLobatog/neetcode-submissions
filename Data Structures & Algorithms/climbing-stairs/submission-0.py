class Solution:
    def climbStairs(self, n: int) -> int:
        # at every step, we can either take 1, or take 2
        # we can keep track of how many steps by simply adding currentStep + 1 or currentStep + 2 
        # once we reach currentStep >= n , add to total
        visited = defaultdict(int)

        def goUp(currentStep):
            nonlocal n, visited

            if currentStep > n:
                return 0
            if currentStep == n:
                return 1

            if currentStep in visited:
                return visited[currentStep]
            
            visited[currentStep] = goUp(currentStep+1) + goUp(currentStep+2)
            return visited[currentStep]

        
        return goUp(0)

        
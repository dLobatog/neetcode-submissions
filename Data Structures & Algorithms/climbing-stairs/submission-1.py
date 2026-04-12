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

        if n <= 2:
            return n 

        # otherwise, you can only come from n-1, or n-2
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n-1]

        
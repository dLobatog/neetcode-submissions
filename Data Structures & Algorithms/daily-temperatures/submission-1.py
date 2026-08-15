class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0 for i in range(len(temperatures))]
        # print(results)

        for i in range(len(temperatures)):
            while len(stack) != 0 and temperatures[i] > stack[-1][0]:
                old_temp, old_i = stack.pop()
                results[old_i] = i - old_i # + 1
        
            stack.append((temperatures[i], i))


        return results
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0: # append positives to the stack
                stack.append(a)
                continue 

            # negatives? pop until top of stack is strictly greater than abs(a)
            # or top of stack is also a negative
            while stack and 0 < stack[-1] < abs(a):
                stack.pop()

            if not stack or stack[-1] < 0:
                stack.append(a) # append another negative
            elif stack[-1] == abs(a):
                stack.pop()     # remove


        return stack

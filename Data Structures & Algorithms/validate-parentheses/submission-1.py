class Solution:
    def isValid(self, s: str) -> bool:
        # correct order checks - seems like stack?
        # len must be %2 ? 
        # if we encounter '(', '[', '{', we push it in the stack
        # if we encounter ')', ']', '}' we pop the stack and check if equivalent pair is found
        # stack must be empty by the end
        stack = []
        parentEquivalence = {
            '[': ']',
            '{': '}',
            '(': ')',
        }

        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            elif char in [')', ']', '}']:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if popped not in parentEquivalence: # wrong order
                    return False
                if parentEquivalence[popped] != char: 
                    return False
        
        return len(stack) == 0
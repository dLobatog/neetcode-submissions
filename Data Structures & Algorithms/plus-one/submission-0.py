class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j = len(digits)-1
        cur = digits[j] + 1
        result = deque()

        if cur < 10:
            return digits[:-1] + [cur]
        else:
            result.append(0)
            j -= 1 
            while j != -1 and digits[j] + 1 == 10:
                j -= 1
                result.appendleft(0)
            
            if j < 0:
                result.appendleft(1)
                return list(result)
            else:
                result.appendleft(digits[j] + 1)
            
            result = digits[:j] + list(result)
        return result

        
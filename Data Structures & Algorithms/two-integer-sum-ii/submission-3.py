class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) -1
        while i < j and i < len(numbers):
            attempt = numbers[i] + numbers[j]
            if attempt == target:
                return [i+1,j+1]
            elif attempt > target:
                j -=1 
            elif attempt < target:
                i += 1
            else:
                i +=1
    
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # majority element in O(1) space
        # split constantly, and return majority elemnt on every split
    
        def f(arr):
            if len(arr) == 1:
                return arr[0]

            half = len(arr) // 2

            left = f(arr[:half])
            right = f(arr[half:])

            if left == right:
                return left

            left_count = arr.count(left)
            right_count = arr.count(right)

            return left if left_count > right_count else right
        
        return f(nums)
            # [3, 3, 4] - half = 1
            # nums[:1] = [3]
            # nums[1:] = [3, 4]
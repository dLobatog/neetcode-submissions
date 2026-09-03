class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (height, left_boundary)
        max_area = 0

        for i, height in enumerate(heights + [0]):
            # print(heights, stack)
            left_boundary = i

            while stack and stack[-1][0] > height:
                popped_height, left_boundary = stack.pop()
                max_area = max(
                    popped_height * (i - left_boundary),
                    max_area
                )
                
            stack.append((height, left_boundary))
            
        return max_area
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (height, left_boundary)
        max_area = 0

        for i, height in enumerate(heights + [0]):
            # print(heights, stack)
            left_boundary = i
            while stack and stack[-1][0] > height:
                popped_height, left_boundary = stack.pop()
                width = i - left_boundary
                area = width * popped_height
                max_area = max(area, max_area)
                
            stack.append((height, left_boundary))
            
        return max_area
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (height, left_boundary)
        max_area = 0

        for i, height in enumerate(heights):
            # print(heights, stack)
            left_boundary = i
            while stack and stack[-1][0] > height:
                popped_height, popped_i = stack.pop()
                width = i - popped_i
                area = width * popped_height
                max_area = max(area, max_area)
                left_boundary = popped_i
                
            stack.append((height, left_boundary))
                            
        i = len(heights)
        while stack:
            popped_height, popped_i = stack.pop()
            width = i - popped_i
            area = width * popped_height
            max_area = max(area, max_area)
            
        return max_area
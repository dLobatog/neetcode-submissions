class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # we need a monotonically growing stack
        # the invariant we are going to keep is: the stack will always contain
        # elements in growing order
        # if we find an element that is not growing, we're going to pop and compute the
        # max area between that element, and continue popping until the invariant is true
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            # print(heights, stack)
            if len(stack) != 0 and stack[-1][0] < height:
                stack.append((height, i))
                continue

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
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def coordinate(position):
            row = position // len(matrix[0])
            col = position % len(matrix[0])
            return row, col 
        
        def bsearch(left, right):
            if left > right or right < left or left < 0 or right >= len(matrix) * len(matrix[0]):
                return False
            mid = (left + right) // 2 
            # need to map this to a 2d grid 
            row, col = coordinate(mid)
            print("checking left, right, mid", left, right, mid)
            print("row, col", row, col)
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
                return False

            value = matrix[row][col]
            print("value", value)
            if value == target:
                return True
            elif value > target:
                return bsearch(left, mid-1)
            elif value < target:
                return bsearch(mid+1, right)

        return bsearch(0, len(matrix) * len(matrix[0]) - 1)
        # [0, 0] [0, 1] [0, 2]
        # [1, 0] [1, 1] [1, 2]
        # [2, 0] [2, 1] [2, 2]
        # to find total elements = len(matrix) * len(matrix[0])
        # if i provide element "8", divide first by rows (8//3 -> 2) 
        # then use remainder for column [2][2], this is 1-indexed
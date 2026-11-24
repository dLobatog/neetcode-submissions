class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.acc = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                prev_row = 0
                prev_col = 0
                overlap = 0
                if r-1 >= 0:
                    prev_row = self.acc[r-1][c]
                if c-1 >= 0:
                    prev_col = self.acc[r][c-1]
                if r-1 >= 0 and c-1 >= 0:
                    overlap = self.acc[r-1][c-1]
                
                self.acc[r][c] = (
                    prev_row + prev_col + matrix[r][c] - overlap
                )

        print(self.acc)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rows_above, cols_to_left, overlap = 0,0,0

        if row1-1 >= 0:
            rows_above = self.acc[row1-1][col2]
        if col1-1 >= 0:
            cols_to_left = self.acc[row2][col1-1]
        if row1-1 >= 0 and col1-1 >= 0:
            overlap = self.acc[row1-1][col1-1]
        return (
            self.acc[row2][col2] -  # bottom-right corner
            rows_above -  # rows above
            cols_to_left +  # cols to the left
            overlap # overlap
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

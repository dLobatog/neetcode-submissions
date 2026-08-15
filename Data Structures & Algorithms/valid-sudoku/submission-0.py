class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        sqrs = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    continue

                sqr = (row // 3, col // 3)

                if (
                    board[row][col] in rows[row] or 
                    board[row][col] in cols[col] or 
                    board[row][col] in sqrs[sqr]
                ):
                    # duplicate found
                    return False

                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                sqrs[sqr].add(board[row][col])

        return True
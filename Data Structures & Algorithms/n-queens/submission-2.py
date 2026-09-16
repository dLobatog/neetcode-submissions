class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        diag_plus = set()
        diag_minus = set()
        cols = set()
        path = []
        results = set()

        def bt(r):
            if r == n:
                results.add(tuple(path))
                return

            for c in range(n):
                d_plus = r + c
                d_min = r - c
                # print(c, d_plus, d_min, cols, diag_plus, diag_minus, path)
                if c not in cols and d_plus not in diag_plus and d_min not in diag_minus:
                    path.append((r,c))
                    diag_plus.add(d_plus)
                    diag_minus.add(d_min)
                    cols.add(c)
                    bt(r+1)
                    path.pop()
                    diag_plus.remove(d_plus)
                    diag_minus.remove(d_min)
                    cols.remove(c)

        bt(0) 
        final = []
        for placement in results:
            board = [['.'] * n for i in range(n)]
            for queen_x, queen_y in placement:
                board[queen_x][queen_y] = 'Q'
            final_board = [''.join(r) for r in board]
            final.append(final_board)

        return final
        # print(final)
        # print(results)
                    
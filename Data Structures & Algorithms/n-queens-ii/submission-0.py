class Solution:
    def totalNQueens(self, n: int) -> int:
        diag_plus = set()
        diag_min = set()
        cols = set()
        results = 0

        def bt(r):
            nonlocal results

            if r == n:
                results += 1
                return

            for c in range(n):
                d_plus = r + c
                d_min  = r - c
                if (
                    c not in cols and 
                    d_plus not in diag_plus and
                    d_min not in diag_min
                ):
                    diag_plus.add(d_plus)
                    diag_min.add(d_min)
                    cols.add(c)
                    bt(r+1)
                    cols.remove(c)
                    diag_plus.remove(d_plus)
                    diag_min.remove(d_min)

        bt(0)
        return results

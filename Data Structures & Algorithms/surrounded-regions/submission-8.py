class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # start from borders
        # if found a 'O' do dfs and mark as S
        # after done, mark every non 'S' as 'X'
        # last round, mark 'S' as 'O' and return
        ROWS, COLS = len(board), len(board[0])
        MOVES = [[-1, 0], [+1, 0], [0, -1], [0, +1]]

        def in_bounds(r, c):
            return r < ROWS and c < COLS and c >= 0 and r >= 0

        def dfs(r, c):
            if not in_bounds(r,c) or board[r][c] != 'O':
                return
            
            board[r][c] = 'S' # for saved
           
            for dr, dc in MOVES:
                dfs(r + dr, c + dc)

        # how to find first row, last row, first col, last col
        for r in [0, ROWS-1]:
            for c in range(COLS):
                if board[r][c] == 'O':
                    dfs(r,c)
        for r in range(ROWS):
            for c in [0, COLS-1]:
                if board[r][c] == 'O':
                    dfs(r,c)

        # print('board post dfs', board)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
                

        
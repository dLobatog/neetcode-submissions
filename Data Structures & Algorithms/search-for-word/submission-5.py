class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # dfs from word? 
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(i, j, k):
            print(i, j, k)
            if k == len(word):
                return True
            
            for dy, dx in moves:
                x, y = i + dy, j + dx
                if x >= 0 and y >= 0 and x < ROWS and y < COLS and (x, y) not in visited and board[x][y] == word[k]:
                    visited.add((x, y))
                    result = dfs(x, y, k + 1)
                    if result == True:
                        return result
                    visited.remove((x, y))

            return False


        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if dfs(i, j, 1):
                        return True
                    visited.remove((i, j))

        return False


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def backtrack(i, j, nextLetterIndex):
            # 1. SUCCESS: If we've matched all letters
            if nextLetterIndex == len(word):
                return True
            
            # 2. BOUNDARIES & FAILURES: Out of bounds, already visited, or wrong letter
            if (i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or 
                (i, j) in visited or board[i][j] != word[nextLetterIndex]):
                return False

            # 3. CHOOSE: Mark this cell as visited
            visited.add((i, j))

            # 4. EXPLORE: Check neighbors for the NEXT letter
            for di, dj in directions:
                if backtrack(i + di, j + dj, nextLetterIndex + 1):
                    return True

            # 5. BACKTRACK: Unmark this cell so other paths can use it
            visited.remove((i, j))
            return False 

        # 6. STARTING POINT: You must try starting from every cell
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
                    return True
        return False
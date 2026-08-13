class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None

    def addWord(self, word):
        node = self 

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.isWord = True
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        # once you have the trie, you need to check dfs the trie from every possible position i think
        ROWS, COLS = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 

            ch = board[r][c]

            if ch == '#' or ch not in node.children:
                return 

            next_node = node.children[ch]

            if next_node.isWord:
                result.append(next_node.word)
                next_node.word = None
                next_node.isWord = False

            board[r][c] = None

            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            board[r][c] = ch


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root)

        return result

            
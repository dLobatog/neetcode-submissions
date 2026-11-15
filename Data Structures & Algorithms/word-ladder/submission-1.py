class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        g = {}
        for s in [beginWord] + wordList:
            g[s] = [] # no neighbors initially since no duplicates
            for i in range(len(s)):
                # remove 1 char 
                rem = s[:i] + '*' + s[i+1:]
                if rem not in g:
                    g[rem] = []
                g[rem].append(s) # original string is a neighbor always
                g[s].append(rem) # removed char is also a neighbor of original

        # BFS from beginWord
        visited = set()
        visited.add(beginWord)
        q = deque()
        q.append((beginWord, 1))
        while q:
            node, count = q.popleft()
            # print(node, count)

            if len(node) == len(beginWord):
                count += 1
            if node == endWord:
                return count//2

            for nei in g[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, count))


        return 0 
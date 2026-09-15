class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def first_diff_char(a, b):
            i, j = 0, 0
            while i < len(a) and j < len(b) and a[i] == b[j]:
                i += 1
                j += 1

            print(i, j, a, b)
            if i == len(a):
                return None       # valid prefix / identical
            if j == len(b):
                return -1         # invalid
            return a[i], b[i]

        # if not even 2 words, then return the first word
        if len(words) < 2:
            return words[0]
        # iterate all words in pair
        # compare until you find the first different character
        graph = defaultdict(list)
        incoming = defaultdict(int)

        for i in range(len(words) - 1):
            word = words[i]
            for c in word:
                incoming[c] += 0
            nxt_word = words[i+1]
            for c in nxt_word:
                incoming[c] += 0
            result = first_diff_char(word, nxt_word)
            if result == -1:
                return ""
            elif result == None:
                continue

            graph[result[0]].append(result[1])
            incoming[result[0]] += 0
            incoming[result[1]] += 1

        print(graph, incoming)
        q = deque()
        for node_id, count in incoming.items():
            if count == 0:
                q.append(node_id)

        if len(q) == 0:
            return '' # no start? cycle?

        result = []
        # print(q)
        while q:
            node_id = q.popleft()
            result.append(node_id)
            for neighbor in graph[node_id]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    q.append(neighbor)
                    
        if len(result) != len(incoming):
            return ''

        # print('reslt', result)
        return ''.join(result)

        
        




    
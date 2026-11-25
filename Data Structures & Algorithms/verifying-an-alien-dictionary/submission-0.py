class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # if words[0][i] == words[1][i] - find first different char
        # that determines words[0][i] < words[1][i] 
        # or if i >= len(words[0]) -> words[0] is shorter than words[1], ok
        # otherwise i >= len(words[1]) - words[0] is the same but longer - return false
        index = {}
        for i, c in enumerate(order):
            index[c] = i

        for i in range(1, len(words)):
            a, b = words[i-1], words[i]
            j = 0
            while j < len(a) and j < len(b) and a[j] == b[j]:
                j += 1

            if j >= len(b):
                # longest word can't be 2nd
                return False

            if j >= len(a):
                # all good
                continue

            # a[j] < b[j]
            if index[a[j]] < index[b[j]]:
                continue
            else:
                return False

        return True


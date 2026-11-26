class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for a, b in zip_longest(word1, word2, fillvalue=''):
            result.append(a)
            result.append(b)

        return ''.join(result)

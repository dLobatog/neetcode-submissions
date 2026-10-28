class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sSet, tSet = Counter(s), Counter(t)

        return sSet == tSet

        
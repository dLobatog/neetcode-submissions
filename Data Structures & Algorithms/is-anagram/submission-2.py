class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # counter_s, counter_t = Counter(s), Counter(t)

        # return counter_s == counter_t

        if len(s) != len(t):
            return False

        counts_s, counts_t = [0] * 26, [0] * 26

        for i in range(len(s)):
            counts_s[ord(s[i]) - ord('a')] += 1
            counts_t[ord(t[i]) - ord('a')] += 1

        return counts_s == counts_t

            
        
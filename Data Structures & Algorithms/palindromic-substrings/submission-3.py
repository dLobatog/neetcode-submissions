class Solution:
    def countSubstrings(self, s: str) -> int:
        # for odd palindromes, assume we start l, r = i
        # never let l and r go out of bounds or l != r
        count = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        # for even palindromes, assume we start l, r = i, i+1
        for i in range(len(s)):
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count

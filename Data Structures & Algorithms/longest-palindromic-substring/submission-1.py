class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(i,j):
            while i >= 0 and j < len(s) and  s[i] == s[j]:
                i -= 1
                j += 1

            return s[i+1:j]

        longest = ''
        for i in range(len(s)):
            # even
            evenP = ''
            if i+1 < len(s):
                evenP = expand(i, i+1)
            # odd
            oddP = expand(i, i)
            # print(evenP, oddP, longest)
            longest = max(oddP, evenP, longest, key=lambda x: len(x))

        return longest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest substring is constrained by start/end indices.
        # counting duplicate characters can be done with a hash of 26 elements
        # that measures ord(char) - ord('a') count
        start = 0
        longestLen = 0
        counter = set()

        for end in range(len(s)):
            
            while s[end] in counter: # shrink window from left
                counter.remove(s[start])
                start += 1
                
            counter.add(s[end])
            longestLen = max(end-start + 1, longestLen)

        return longestLen        
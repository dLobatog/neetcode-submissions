class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        "pwwkew"

        l, r = 0, 1
        [p]
        1st iter
        w not in [p] - [pw], r=2, result=max(1, 2-0)=2
        2nd iter
        w in p... you shouldn't remove l! you should remove pos of w.
        """
        if len(s) <= 1:
            return len(s)

        windowSet = {} # this maintains unique chars
        l, r = 0, 1
        result = 1
        windowSet[s[l]] = l
        while r < len(s):
            if s[r] in windowSet:
                # restart window from windowSet[s[r]] onwards
                # move l to windowSet[s[r]] pos
                i = l
                while s[r] in windowSet and i <= windowSet[s[r]]:
                    # print(i, windowSet, windowSet[s[i]])
                    del windowSet[s[i]]
                    i += 1
                l = i
                
            windowSet[s[r]] = r
            r += 1
            result = max(result, r-l)

        return result


        


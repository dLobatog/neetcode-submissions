class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # up to k characters and replace with ANY other (28 max possibilities)
        # what is the length of the longest substring containing only 1 distinct character
        # which characters would you replace to make all its characters identical
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                # we will move this and count how many are equal to c 
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k: # replacements < k
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r-l+1)

        return res
            

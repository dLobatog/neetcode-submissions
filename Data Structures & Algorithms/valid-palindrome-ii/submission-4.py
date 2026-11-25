class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(arr):
            l, r = 0, len(arr)-1
            while l < r:
                if arr[l] != arr[r]:
                    return False
                l += 1
                r -= 1

            return True


        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                return isPalindrome(s[l:r]) or isPalindrome(s[l+1:r+1])
            l += 1
            r -= 1

        return True
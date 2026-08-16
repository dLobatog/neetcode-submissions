class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # fixed size, sliding window of s1
        #. try to go over s2, counting frequencies. 
        #  keep s1 freq array and s2 freq array in check 
        #.   if ever same, then you found the window
        if len(s2) < len(s1):
            return False

        freqS1, freqS2 = [0 for i in range(26)], [0 for i in range(26)]
        matches = 0

        for c in s1:
            freqS1[ord(c) - ord('a')] += 1

        for i in range(len(s1)):
            freqS2[ord(s2[i]) - ord('a')] += 1

        if freqS1 == freqS2:
            return True

        left = 0

        # print(freqS1, freqS2)
        for right in range(len(s1), len(s2)):
            freqS2[ord(s2[right]) - ord('a')] += 1    
            
            freqS2[ord(s2[left]) - ord('a')] -= 1
            left += 1

            if freqS1 == freqS2:
                return True

        
        return False
        
        
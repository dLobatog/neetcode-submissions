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

        i, j = 0, len(s1)-1

        # print(freqS1, freqS2)
        while j < len(s2) - 1:
            print(freqS1, freqS2)
            if freqS1 == freqS2:
                return True

            # take 1st char, remove from count, then increase i
            freqS2[ord(s2[i]) - ord('a')] -= 1
            i += 1
            # increase j, and add it to window
            j += 1
            freqS2[ord(s2[j]) - ord('a')] += 1    
        
        return freqS1 == freqS2
        
        
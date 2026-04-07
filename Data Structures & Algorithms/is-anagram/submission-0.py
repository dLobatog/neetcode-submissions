class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s, counter_t = Counter(s), Counter(t)

        return counter_s == counter_t
            
        
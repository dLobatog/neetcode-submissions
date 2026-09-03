class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # substric, such that every charachter in t, is present in the substring
        if len(t) > len(s): 
            return ""

        count = Counter(t) # { X: 1, Y: 1, Z: 1 }
                
        def valid_window(count):
            all_zero = True
            for key, value in count.items():
                all_zero = all_zero and value <= 0 
            
            return all_zero
        
        l = 0 
        min_length = float('inf')
        min_left = -1
        min_right = -1
        for r, right_char in enumerate(s):
            if right_char in count:
                count[right_char] -= 1

            # check are all elements 0:
            while valid_window(count):
                # compare s[l:r+1] with best window
                window_length = r - l + 1
                if window_length < min_length:                    
                    min_length = window_length
                    min_left = l
                    min_right = r

                # take out s[l]
                left_char = s[l]
            
                if left_char in count:
                    count[left_char] += 1

                l += 1

        if min_length == float('inf'):
            return ""

        return s[min_left:min_right+1]




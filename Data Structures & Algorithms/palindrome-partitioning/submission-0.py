class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        current = []

        def f(start):
            if start == len(s):
                # found complete partition
                results.append(current.copy())
                return 

            for end in range(start+1, len(s)+1):
                substring = s[start:end]

                if substring == substring[::-1]:
                    # choose substring
                    current.append(substring)
                    # explore remaining chars
                    f(end)
                    # undo choice
                    current.pop()
        
        f(0)

        return results
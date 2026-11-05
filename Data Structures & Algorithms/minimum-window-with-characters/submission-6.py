class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        counter = Counter(t)
        checks = counter.copy()
        required = len(counter)
        satisfied = 0

        l, r = 0, 0
        shortest_subst = None
        # print(checks)
        while r < len(s):
            # expand window to the right and check, are all zeros?
            if s[r] in checks:
                checks[s[r]] -= 1
                if checks[s[r]] == 0:
                    # print('satisfied ', s[r])
                    satisfied += 1

            # if all satisfied, close the window from the left
            if satisfied == required:
                # print("before", s[l:r+1], l, r)
                while satisfied == required:
                    if s[l] in checks:
                        checks[s[l]] += 1
                        if checks[s[l]] > 0:
                            satisfied -= 1 # this is enough to stop here!
                    l += 1
                
                # we go back to just before breaking satisfied == required
                l -= 1
                checks[s[l]] -= 1
                satisfied += 1
                # print("after", s[l:r+1], l, r)
                if shortest_subst:
                    shortest_subst = s[l:r+1] if len(s[l:r+1]) < len(shortest_subst) else shortest_subst
                else:
                    shortest_subst = s[l:r+1]
            r += 1

        return shortest_subst if shortest_subst else ""
            
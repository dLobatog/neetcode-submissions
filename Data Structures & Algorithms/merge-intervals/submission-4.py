class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # [start, end],
        # we begin with first interval, save as "temp"
        #   if next interval start <= first interval end... merge (set temp end to "next end")
        #   else: create new temp; and save the previous one to the list of results
        results = []
        intervals.sort(key=lambda x: x[0])
        curr = [intervals[0][0], intervals[0][1]]
        for next_start, next_end in intervals[1:]:
            if next_start <= curr[1]:
                curr[1] = max(next_end, curr[1])
                curr[0] = min(next_start, curr[0])
            else:
                results.append(curr)
                curr = [next_start, next_end]
        results.append(curr)
        return results        

            

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start 
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        results = []
        cur = [sorted_intervals[0][0], sorted_intervals[0][1]]
        for start_new, end_new in sorted_intervals[1:]:
            if start_new > cur[1]: # new interval
                results.append(cur)
                cur = [start_new, end_new]
            elif start_new <= cur[1]:
                cur[1] = max(cur[1], end_new) # merge

        results.append(cur)
        return results


        # [1, 2] = cur
        # [2, 3] = start_new, end_new
        # 2 < start_new? no, they're the same...
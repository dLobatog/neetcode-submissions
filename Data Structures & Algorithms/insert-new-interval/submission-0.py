class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals [start, end] of a time
        # insert so that they are still in sorted order
        # to be in sorted order:
        # start time newInterval < start time of an interval in intervals we gotta find
        # then we handle merging 
        # [1, 3] , [4, 6] - new interval [2, 5]
        # ---------------
        #.  1--3
        #.        4--6
        #.    2----5
        #. keep index. if at any point newInterval start > intervals[i][start]
        # insert interval on intervals[i-1]
        #   if newInterval[end] < intervals[i][end] - then we can just insert it in the previous position
        #.       no merging needed
        #.      intervals.append(newInterval)
        #.  otherwise, we need to merge until intervals[end] < newInterval[end] - then append
        #      intervals.append((newInterval[start], intervals[i][end]))
        #.     if we got to the very end (i == len(intervals) - then append with original length)
        START, END = 0, 1
        i = 0 
        sorted = []
        appended = False
        for interval in intervals:
            if not appended and newInterval[START] < interval[START]:
                sorted.append(newInterval)
                appended = True
            sorted.append(interval)
    
        if not appended:
            sorted.append(newInterval)

        result = [sorted[0]]
        for i in range(1, len(sorted)):
            current = result[-1]
            if current[END] >= sorted[i][START]:
                current[END] = max(current[END], sorted[i][END])
            else:
                result.append(sorted[i])


        return result
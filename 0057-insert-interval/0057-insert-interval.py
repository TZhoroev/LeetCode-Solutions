class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #base case
        if len(intervals) == 0: return [newInterval]
        ans = []
        for i in range(len(intervals)):
            # if new interval's start is greater than end of current interval
            if newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])
            # if new interval's end is less than end of current interval
            elif newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                return ans + intervals[i:]
            # if current interval and new interval is overlapping, then extend the interval.
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        ans.append(newInterval)

        return ans
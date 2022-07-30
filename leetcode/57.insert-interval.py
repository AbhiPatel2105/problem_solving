#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][1] and newInterval[1] >= intervals[i][0]:
                j = i + 1
                k = intervals[i][1]
                while(j < len(intervals) and intervals[j][0] <= newInterval[1]):
                    k = intervals[j][1]
                    intervals.remove(intervals[j])
                intervals[i][0] = min(newInterval[0],intervals[i][0])
                intervals[i][1] = max(k, newInterval[1])                 
                return intervals 
            if newInterval[0] < intervals[i][0]:
                intervals.insert(i, newInterval)
                j = i + 1
                k = intervals[i][1]
                flag = False
                while(j < len(intervals) and intervals[j][0] <= newInterval[1]):
                    k = intervals[j][1]
                    intervals.remove(intervals[j])
                    flag = True
                if flag:
                    intervals[i][0] = min(newInterval[0],intervals[i][0])
                    intervals[i][1] = max(k, newInterval[1])                 
                return intervals 
        intervals.append(newInterval)
        return intervals
# @lc code=end


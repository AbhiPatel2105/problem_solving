#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
import queue


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m  = Counter(tasks)
        q = queue.PriorityQueue()
        for key in m.keys():
            q.put([key,m[key]])
        count = 0
        stack = []
        while not q.empty():
                        
    
# @lc code=end


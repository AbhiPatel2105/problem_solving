#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        last,second_last = 3,2
        for i in range(4,n+1):
            temp = last + second_last
            second_last = last
            last = temp
        return last
# @lc code=end


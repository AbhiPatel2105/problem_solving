#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        any = []
        while(True):
            n = str(n)
            sum = 0
            for i in range(len(n)):
                sum += int(n[i])*int(n[i])
            if sum == 1:
                return True
            if sum in any:
                return False
            n = sum
            any.append(n)
# @lc code=end


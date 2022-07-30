#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = nums[0]
        sum1 = nums[0]
        for i in range(1,len(nums)):
            if sum1 < 0:
                sum1 = 0
            sum1 += nums[i]
            if sum1 > max:
                max = sum1
        return max
# @lc code=end


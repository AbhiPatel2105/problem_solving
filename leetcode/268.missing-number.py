#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)*(len(nums) + 1)//2
        for ele in nums:
            res -= ele
        return res
# @lc code=end


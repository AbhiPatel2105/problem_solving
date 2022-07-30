#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        if len(nums) == 3:
            return max((nums[0] + nums[2]),nums[1])
        ans = [0]*len(nums)
        ans[-1] = nums[-1]
        ans[-2] = nums[-2]
        ans[-3] = nums[-3] + nums[-1]
        for i in range(len(nums) - 4,-1,-1):
            ans[i] = max(ans[i + 2], ans[i + 3]) + nums[i]
        return max(ans[0],ans[1])
# @lc code=end


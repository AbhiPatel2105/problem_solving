#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = [0]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= len(nums):
                ans[i] = 1
            elif nums[i] == 0:
                ans[i] = float("inf")
            else:
                ans[i] = min(ans[i+1:i+1+nums[i]]) + 1
        return ans[0]
# @lc code=end


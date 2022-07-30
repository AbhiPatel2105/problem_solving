#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums1: List[int]) -> int:
        if len(nums1) == 1:
            return nums1[0]
        def func(nums):
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
        ans1 = func(nums = nums1[0:len(nums1) - 1])
        ans2 = func(nums = nums1[1:])
        return max(ans1,ans2)
# @lc code=end


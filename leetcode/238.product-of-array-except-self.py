#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        ans = []
        for i in range(len(nums)):
            ans.append(prefix)
            prefix *= nums[i]
        postfix = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans 
        
# @lc code=end


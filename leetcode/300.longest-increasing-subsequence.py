#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [1]*len(nums)
        for i in range(len(ans) - 2,-1,-1):
            for j in range(i + 1,len(ans)):
                if nums[i] < nums[j] and ans[j] + 1 > ans[i]:
                    ans[i] = ans[j] + 1
        return max(ans)  
# @lc code=end


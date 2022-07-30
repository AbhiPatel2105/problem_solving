#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        res = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                count += 1
                continue
            print(count)
            print(nums[i-1],nums[i])
            if nums[i-1] == nums[i]:
                continue
            if nums[i-1] + 1 == nums[i]:
                count += 1
            else:
                res = max(res,count)
                count = 1
        res = max(res,count)
        return res
                
# @lc code=end


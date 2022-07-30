#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        nums = list(set(nums))
        if len_nums == len(nums):
            return False
        return True
# @lc code=end


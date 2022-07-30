#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans = can_we(nums,index = len(nums) - 1)
        return ans

def can_we(nums,index):
    if index == 0:
        return True
    for i in range(index - 1,-1,-1):
        if nums[i] + i >= index:
            index = i
    if index == 0:
        return True
    return False
        
# @lc code=end


#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while(k > len(nums)):
            k -= len(nums)
        high = -1
        low = -k
        while(low <= high):
            nums[low],nums[high] = nums[high],nums[low]
            low += 1
            high -= 1
        low = 0
        high = len(nums) - k - 1
        while(low <= high):
            nums[low],nums[high] = nums[high],nums[low]
            low += 1
            high -= 1
        low = 0
        high = len(nums) - 1
        while(low <= high):
            nums[low],nums[high] = nums[high],nums[low]
            low += 1
            high -= 1
        return nums
# @lc code=end


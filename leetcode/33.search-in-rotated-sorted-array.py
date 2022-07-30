#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high = 0,len(nums)-2
        flag = False
        while(low<=high):
            mid = (low + high)//2
            if nums[mid] > nums[mid+1]:
                flag = True
                i = mid + 1
                break
            if nums[mid] < nums[low]:
                high = mid - 1
            else:
                low = mid + 1
        if flag ==  False:
            i = 0
        if target >= nums[i] and target <= nums[-1]:
            low,high = i,len(nums)-1
        else:
            low,high = 0,i-1
        while(low<=high):
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
# @lc code=end


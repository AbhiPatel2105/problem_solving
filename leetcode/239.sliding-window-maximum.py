#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        i,j = 0,k
        ans.append(max(nums[i:j]))
        while(j < len(nums)):
            i += 1
            j += 1
            if nums[j - 1] >= ans[-1]:
                ans.append(nums[j - 1])
            elif ans[-1] == nums[i - 1]:
                ans.append(max(nums[i:j]))
            else:
                ans.append(ans[-1])
        return ans
# @lc code=end


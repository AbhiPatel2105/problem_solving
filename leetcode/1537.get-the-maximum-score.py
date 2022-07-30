#
# @lc app=leetcode id=1537 lang=python3
#
# [1537] Get the Maximum Score
#

# @lc code=start
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        temp1 = temp2 = i = j = ans = 0
        while(i < len(nums1) and j < len(nums2)):
            if nums1[i] == nums2[j]:
                ans += max(temp1,temp2) + nums1[i]
                temp1 = temp2 = 0
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                temp1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                temp2 += nums2[j]
                j += 1

        while(i < len(nums1)):
            temp1 += nums1[i]
            i += 1
        while(j < len(nums2)):
            temp2 += nums2[j]
            j += 1
        return ans + max(temp1,temp2)
# @lc code=end


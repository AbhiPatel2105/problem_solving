#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[],[nums[0]]]
        for i in range(1,len(nums)):
            temp1 = []
            for j in range(len(ans)):
                temp = copy.deepcopy(ans[j])
                temp.append(nums[i])
                temp1.append(temp)
            for j in range(len(temp1)):
                ans.append(temp1[j])
        return ans
# @lc code=end


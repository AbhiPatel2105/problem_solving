#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            for i in range(len(ans)-1,-1,-1):
                temp = []
                ele = ans[i]
                for i in range(len(ans[i]) + 1):
                    ele1 = copy.deepcopy(ele)
                    ele1.insert(i, num)
                    temp.append(ele1)
                ans.remove(ele)
                for ele in temp:
                    ans.append(ele)
        return ans
                
# @lc code=end


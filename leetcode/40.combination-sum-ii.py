#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def dfs(i,temp = []):
            sum_temp = sum(temp)
            if i >= len(candidates) or candidates[i] + sum_temp > target:
                return 
            if candidates[i] + sum_temp == target:
                temp.append(candidates[i])
                ans.append(temp)
                return 
            any1 = copy.deepcopy(temp)
            any2 = copy.deepcopy(temp)
            any1.append(candidates[i])
            dfs(i + 1,any1)
            while(i < len(candidates) - 1 and candidates[i] == candidates[i + 1]):
                i += 1
            dfs(i + 1,any2)
        dfs(0)
        return ans
# @lc code=end


#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def dfs(i,temp = []):
            if i >= len(candidates):
                return
            sum_temp = sum(temp)
            if candidates[i] + sum_temp == target:
                temp.append(candidates[i])
                ans.append(temp)
                return
            elif candidates[i] + sum_temp > target:
                return
            any1 = copy.deepcopy(temp)
            any2 = copy.deepcopy(temp)
            any1.append(candidates[i])
            dfs(i,any1)
            dfs(i + 1,any2)
        dfs(0)
        return ans
# @lc code=end


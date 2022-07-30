#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = []
        for i in range(m):
           ans.append([0]*n) 
        ans[-1] = [1]*n
        for i in range(m):
            ans[i][n-1] = 1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                ans[i][j] = ans[i+1][j] + ans[i][j+1]
        return ans[0][0]
# @lc code=end


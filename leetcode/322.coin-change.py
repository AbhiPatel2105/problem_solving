#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # ans  = [0]*(amount + 1)
        # for i in range(1,amount + 1):
        #     if i in coins:
        #         ans[i] = 1
        #         continue
        #     l,r,temp = 1,i - 1,float("inf")
        #     while(l <= r):
        #         if ans[l] != -1 and ans[r] != -1 and ans[l] + ans[r] < temp:
        #             temp = ans[l] + ans[r]
        #         l += 1
        #         r -= 1 
        #     if temp == float("inf"):
        #         ans[i] = -1
        #     else:
        #         ans[i] = temp
        # print(ans)
        # return ans[amount]
        dp = [amount + 1] * (amount + 1) 
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
# @lc code=end


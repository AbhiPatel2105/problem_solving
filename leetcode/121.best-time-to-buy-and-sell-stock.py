#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from cmath import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp_min = []
        var_min = float(inf)
        var_max = float(-inf)
        temp_max = [0]*len(prices)
        for price in prices:
            var_min = min(var_min, price)
            temp_min.append(var_min)
        print(temp_min)
        for i in range(len(prices) - 1,-1,-1):
            var_max = max(var_max, prices[i])
            temp_max[i] = var_max
        print(temp_max)
        ans = 0
        for i in range(len(prices) - 1):
            ans = max(ans,temp_max[i]-temp_min[i])
        return ans
# @lc code=end


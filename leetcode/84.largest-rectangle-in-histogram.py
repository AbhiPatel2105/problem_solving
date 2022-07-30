#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [[0,heights[0]]]
        ans = 
        for i in range(1,len(heights)):
            x = i
            while(x - 1 >= 0 and heights[x - 1] > heights[i]):
                area = 
            
# @lc code=end


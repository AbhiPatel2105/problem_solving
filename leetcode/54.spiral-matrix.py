#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        total = len(matrix)*len(matrix[0])
        i_up = 0
        i_down = len(matrix)
        j_left = 0
        j_right = len(matrix[0])
        ans = []
        while(total >= 1):
            for k in range(j_left,j_right):
                ans.append(matrix[i_up][k])
                 
                total -= 1
            i_up += 1
            for k in range(i_up,i_down):
                ans.append(matrix[k][j_right-1])
                 
                total -= 1
            j_right -= 1
            if not (j_left < j_right and i_up < i_down):
                break
            for k in range(j_right - 1,j_left-1,-1):
                ans.append(matrix[i_down - 1][k])
                 
                total -= 1
             
            i_down -= 1
            for k in range(i_down - 1,i_up-1,-1):
                ans.append(matrix[k][j_left])
                 
                total -= 1
             
            j_left += 1
            # break
        return ans
# @lc code=end


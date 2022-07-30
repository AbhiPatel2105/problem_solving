#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        total = len(matrix)*len(matrix[0])
        i_up = 0
        i_down = len(matrix)
        j_left = 0
        j_right = len(matrix[0])
        while(total >= 1):
            temp1 = []
            for k in range(j_left,j_right):
                temp1.append(matrix[i_up][k])
                 
                total -= 1
            i_up += 1
            temp1.reverse()
            temp2 = []
            for k in range(i_up,i_down):
                temp2.append(matrix[k][j_right-1])
                matrix[k - 1][j_right-1] = temp1.pop()
                total -= 1
            matrix[k][j_right-1] = temp1.pop()
            j_right -= 1
            temp2.reverse()
            if not (j_left < j_right and i_up < i_down):
                break
            temp1 = []
            for k in range(j_right - 1,j_left-1,-1):
                temp1.append(matrix[i_down - 1][k])
                matrix[i_down - 1][k] = temp2.pop()
                total -= 1
            temp1.reverse()
            i_down -= 1
            k = i_up
            for k in range(i_down - 1,i_up-1,-1):
                temp2.append(matrix[k][j_left])
                matrix[k][j_left] = temp1.pop()
                total -= 1
            matrix[k - 1][j_left] = temp1.pop()
            j_left += 1
            temp2.reverse()
            for k in range(j_left,j_right):
                matrix[i_up - 1][k] = temp2.pop()
        
        
            
        
# @lc code=end


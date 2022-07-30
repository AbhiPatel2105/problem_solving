#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        column = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                   row.add(i)
                   column.add(j)
        for ele in row:
            matrix[ele] = [0]*len(matrix[0])
        for ele in column:
            for i in range(len(matrix)):
                matrix[i][ele] = 0
        return matrix
        
# @lc code=end


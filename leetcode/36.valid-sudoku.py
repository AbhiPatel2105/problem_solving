#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for ele in board:
            if not contain_duplicate(ele):
                print(ele)
                return False
        for i in range(9):
            arr = []
            for ele in board:
                arr.append(ele[i])
            if not contain_duplicate(arr):
                print(arr)
                return False
        start_i = 0
        start_j = -3
        while(True):
            arr = []
            start_j += 3
            
            for i in range(start_i,start_i + 3):
                for j in range(start_j,start_j + 3):
                    # print(i,j)
                    arr.append(board[i][j])
            
            if not contain_duplicate(arr):
                print(arr)
                return False
            # start_j += 3
            if start_j + 3 == 9:
                start_j = -3
                start_i += 3
            if start_i == 9:
                break
        return True
def contain_duplicate(arr):
    dicti={}
    for i in arr:
        if i == ".":
            continue
        if i not in dicti:
            dicti[i]=1
        else:
            return False
        
    return True
# @lc code=end


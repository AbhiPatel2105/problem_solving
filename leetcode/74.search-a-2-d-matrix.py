#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for ele in matrix:
            if target >= ele[0] and target <= ele[-1]:
                ans = search(ele,target,0,len(ele)-1)
                return ans
def search(ele,target,low,high):
    mid = (low + high)//2
    if low > high:
        return False
    if target == ele[mid]:
        return True
    elif target > ele[mid]:
        return search(ele,target,mid + 1,high)
    else:
        return search(ele,target,low,mid-1)
         
# @lc code=end


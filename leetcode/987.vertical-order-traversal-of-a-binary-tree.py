#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        brr = [""]
        def tra(root,level,h):
            if root is None:
                return
            if level >= 0:
                if len(arr) == level:
                    arr.append([root.val])
                else:
                    arr[level].append(root.val)
            else:
                if len(brr) == abs(level):
                    brr.append([root.val])
                else:
                    brr[abs(level)].append(root.val) 
            # tra(root.left,level-1)
            # tra(root.right,level+1)
            return
        tra_arr = [[root,0]]
        while(len(tra_arr) > 0):
            ele = tra_arr.pop(0)
            tra(ele[0],ele[1])
            if ele[0] is None:
                continue
            tra_arr.append([ele[0].left,ele[1]-1])
            tra_arr.append([ele[0].right,ele[1]+1])
        # tra(root,0)
        ans = []
        for i in range(len(brr)-1,0,-1):
            ans.append(brr[i])
        for i in range(len(arr)):
            ans.append(arr[i])
        return ans
# @lc code=end


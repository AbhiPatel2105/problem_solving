#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ans = []
        def tra(root,temp):
            if root.left is None and root.right is None:
                ans.append(temp)
            elif root.left is not None and root.right is not None:
                tra(root.left,temp+1)
                tra(root.right,temp+1)
            elif root.left is not None and root.right is None:
                tra(root.left,temp+1)
            else:
                tra(root.right,temp+1)
        tra(root,1)
        return min(ans)                
            
# @lc code=end


#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def tra(root1,root2):
            if root1 is None and root2 is None:
                return True
            if root1.left is None or root2.right is None:
                if root1.left is None and root2.right is None:
                    flag1 = True
                else:
                    flag1 = False
            elif root1.left.val == root2.right.val:
                flag1 = tra(root1.left,root2.right)
            else:
                flag1 = False
            if root1.right is None or root2.left is None:
                if root1.right is None and root2.left is None:
                    flag2 = True
                else:
                    flag2 = False
            elif root1.right.val == root2.left.val:
                flag2 = tra(root1.right,root2.left)
            else:
                flag2 = False
            return flag1 and flag2
        return tra(root,root)
# @lc code=end


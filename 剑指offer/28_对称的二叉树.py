# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(l, r):
            if not l and not r:
                return True
            if not l or not r or l.val != r.val:
                return False
            return recur(l.left, r.right) and recur(l.right, r.left)
        return recur(root.left, root.right) if root else True
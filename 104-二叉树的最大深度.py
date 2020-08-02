# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 递归
        # l = self.maxDepth(root.left)
        # r = self.maxDepth(root.right)
        # return max(l, r) +1

        # BFS
        q = [root]
        level = 0
        while q:
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            level += 1
        return level

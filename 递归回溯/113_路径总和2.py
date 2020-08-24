# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []
        def dfs(root, tar):
            if not root:
                return
            tar -= root.val
            path.append(root.val)
            if tar == 0 and not root.left and not root.right:
                res.append(path[:])
            dfs(root.left, tar)
            dfs(root.right, tar)
            path.pop()
        dfs(root, sum)
        return res
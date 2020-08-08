"""
先序遍历： 按照 “根、左、右” 的顺序，遍历树的所有节点。
路径记录： 在先序遍历中，记录从根节点到当前节点的路径。当路径为 ① 根节点到叶节点形成的路径 且 ② 各节点值的和等于目标值 sum 时，将此路径加入结果列表。

"""


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
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(path.copy())
            dfs(root.left, tar)
            dfs(root.right, tar)
            path.pop()
        dfs(root, sum)
        return res
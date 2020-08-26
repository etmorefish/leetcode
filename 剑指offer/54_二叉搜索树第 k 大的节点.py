# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
二叉搜索树的一个特性：通过中序遍历所得到的序列，就是有序的
# 根据以上性质，易得二叉搜索树的 中序遍历倒序 为 递增序列 。
# 因此，求 “二叉搜索树第 k 大的节点” 可转化为求 “此树的中序遍历倒序的第 kk 个节点”。
'''


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.res, self.k = None, k

        def dfs(node):
            if not node:
                return
            else:
                # 中序遍历倒序
                dfs(node.right)
                self.k -= 1
                if self.k == 0:
                    self.res = node.val
                if self.k > 0:
                    dfs(node.left)

        dfs(root)
        return self.res


        # 2
        def helper(root):
            return helper(root.left) + [root.val] + helper(root.right) if root else []

        return helper(root)[-k]

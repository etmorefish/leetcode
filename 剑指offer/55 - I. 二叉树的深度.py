'''二叉树的深度（后序遍历、层序遍历
树的遍历方式总体分为两类：深度优先搜索（DFS）、广度优先搜索（BFS）；

常见的 DFS ： 先序遍历、中序遍历、后序遍历；
常见的 BFS ： 层序遍历（即按层遍历）。


'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        # 方法一：后序遍历（DFS） 递归

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # 方法二：层序遍历（BFS）
        queue, res = [root], 0
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            res += 1
        return res

        # 方法三：层序遍历（BFS） 同时遍历层数
        stack = [(root, 1)]
        while stack:
            node, res = stack.pop(0)
            if node.left:
                stack.append(node.left, res+1)
            if node.right:
                stack.append(node.right, res +1)
        return res
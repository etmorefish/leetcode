# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # 递归
        # if not root:
        #     return False
        # if not root.left and not root.right:
        #     return sum == root.val
        # return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

        # dfs 回溯
        def dfs(root, tar):
            if not root:
                return False
            tar -= root.val
            # path.append(root.val)
            if tar == 0 and not root.left and not root.right:
                return True
            left_flag, right_flag = False, False
            if root.left:
                left_flag = dfs(root.left, tar)
            if root.right:
                right_flag = dfs(root.right, tar)
            # path.pop()
            return left_flag or right_flag

        return dfs(root, sum)

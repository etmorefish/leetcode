# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def dfs(A, B):
            if not B:
                # b都遍历完了，还没发现不一样的，说明那就一样了
                return True
            if not A:
                # 没有a，当然不行
                return False
            if A.val != B.val:
                # a b 的值不相等，肯定不行
                return False
            return dfs(A.left, B.left) and dfs(A.right, B.right)

        if not A or not B:
            return False
        # 如果直接给的 A B 两棵树满足条件，直接返回True
        return dfs(A, B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right, B)
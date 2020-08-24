class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def dfs(A, B):
            if A in None or B is None:
                return False

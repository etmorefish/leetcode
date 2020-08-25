# 矩阵中的路径

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 深度优先搜索（DFS）+ 剪枝 解决
        def dfs(i, j, k):
            # 终止条件
            if not 0 <= i < len(board) or not 0 <= len(board[0]) or board[i][j] != word[k]:
                return False
            # 字符串已經完全匹配
            if k == len(word) - 1:
                return True
            tmp, board[i][j] = board[i][j], '/'
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k+1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:

        # 模仿第47题，全排列  dfs写法 递归回溯
        def dfs(s, visited, path, depth, res):
            if depth == len(s):
                res.append(''.join(path[:]))  # 深度复制 列表变字符串
                return
            for i in range(len(s)):
                if not visited[i]:
                    # 剪枝
                    if i > 0 and s[i] == s[i - 1] and not visited[i - 1]:
                        continue
                    visited[i] = True  # 设置现场
                    path.append(s[i])
                    dfs(s, visited, path, depth + 1, res)  # 递归
                    visited[i] = False  # 恢复现场
                    path.pop()

        visited = [False for _ in range(len(s))]
        path = []
        depth = 0
        res = []
        s = [_ for _ in s]  # 字符串变列表
        s.sort()
        dfs(s, visited, path, 0, res)
        return res


if __name__ == '__main__':
    s = 'abc'
    # s = [_ for _ in s]
    solution = Solution()
    res = solution.permutation(s)
    print(res)

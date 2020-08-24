"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
import copy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, visited, path, depth, res):
            if depth == len(nums):
                res.append(path[:])  # 深度复制
                return
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True  # 1.设置现场
                    path.append(nums[i])
                    dfs(nums, visited, path, depth + 1, res)  # 2.递归
                    visited[i] = False  # 恢复现场
                    path.pop()

        visited = [False for _ in range(len(nums))]
        path = []
        depth = 0
        res = []
        dfs(nums, visited, path, depth, res)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)

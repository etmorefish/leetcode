"""
当 gridgrid 矩阵很大时， i = 0i=0 或 j = 0j=0 的情况仅占极少数，
相当循环每轮都冗余了一次判断。因此，可先初始化矩阵第一行和第一列，再开始遍历递推。


"""

from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = [(0,0)]
        for i in range(1, m):    # 初始化第一行
            grid[i][0] += grid[i -1][0]
        # print(grid)
        for j in range(1, n):   # 初始化第一列
            grid[0][j] += grid[0][j-1]
        # print(grid)

        for i in range(1, m):
            for j in range(1,n):
                grid[i][j] += max(grid[i][j-1], grid[i-1][j])
                # res.append((i,j))
        # print(grid)
        return grid[-1][-1]

    def maxValue2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = [(0,0)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j -1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += max(grid[i][j-1], grid[i-1][j])
                # res.append((i,j))
        # print(grid)
        return grid[-1][-1]

a = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
'''
1 4 5
2 9 10
6 11 12


'''
# 1→3→5→2→1   1 5 121
b = [[1,2,5],
     [3,2,1]]
# print(Solution().maxValue(b))
print(Solution().maxValue2(a))
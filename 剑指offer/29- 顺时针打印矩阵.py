"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
输入：matrix =  [[1,2,3],
                [4,5,6],
                [7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
-2 1
"""


class Solution:
    def spiralOrder(matrix):
        ret = []
        y = len(matrix)  # 3
        x = len(matrix[0])  # 4
        for i in range(x):
            print(matrix[0][i] , end=' ')
        for j in range(x-1):
            print(matrix[j][y] , end=' ')
        for k in range(x):
            print(matrix[x -1][k] , end=' ')

        return ret


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# [1,2,3,4,8,12,11,10,9,5,6,7]
print(Solution.spiralOrder( matrix))
"""
根据题目示例 matrix = [[1,2,3],[4,5,6],[7,8,9]] 的
对应输出 [1,2,3,6,9,8,7,4,5] 可以发现，
顺时针打印矩阵的顺序是 “从左向右、从上向下、从右向左、从下向上” 循环。
（模拟、设定边界，清晰图解）
"""
class Solution:
    # def spiralOrder(self, matrix):
    #     res = []
    #     while matrix:
    #         res += matrix.pop(0)
    #         matrix = list(zip(*matrix))[::-1]      # 压缩与解压缩
    #     return res

    def spiralOrder(self, matrix):
        if not matrix: return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1): 
                res.append(matrix[t][i]) # left to right
            t += 1
            if t > b: break
            for i in range(t, b + 1): 
                res.append(matrix[i][r]) # top to bottom
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1): 
                res.append(matrix[b][i]) # right to left
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1): 
                res.append(matrix[i][l]) # bottom to top
            l += 1
            if l > r: break
        return res

            



s = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(s.spiralOrder(matrix))
# [1, 2, 3, 6, 9, 8, 7, 4, 5]
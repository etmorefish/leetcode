class Solution:
    # array 二维列表
    def Find(self, target, array):  # O(n2)
        # write code here
        if array == []:
            return False
        else:
            for i in range(len(array)):
                for j in range(len(array[i])):
                    if target == array[i][j]:
                        return True
            return False

    # 从右上角往左下角找
    def find(self, target, array):  # O(n)
        if array == [] or array == [[]]:
            return False
        row_count = len(array)
        column_count = len(array[0])
        i = 0
        j = column_count-1
        while i < row_count and j > 0:
            values = array[i][j]
            if values == target:
                return True
            elif values > target:
                j -= 1
            else:
                i += 1
        return False


    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        return False



array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
s = Solution()
# print(s.Find(8, array))
print(s.find(9, array))
print(s.Find(7, [[1, 2, 8, 9], [4, 7, 10, 13]]))
print(s.find(5, [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]))
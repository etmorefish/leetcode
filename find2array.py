'''
题目：
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

class Solution:
    # array 二维列表
    def find(self, target, array):
        for i in range(len(array) - 1, -1, -1):
            if target == array[i][0]:
                # print('ok')
                return True
            elif target > array[i][0]:
                for j in range(len(array[0])):
                    if target == array[i][j]:
                        # print('ok')
                        return True
            else:
                # print('not find')
                return False

array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
s = Solution()
print(s.find(8, array))
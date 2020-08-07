# -*- coding:utf-8 -*-
"""
我们可以用2 1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2 1的小矩形无重叠地覆盖一个2 n的大矩形，总共有多少种方法？
"""
class Solution:
    def rectCover(self, number):
        # write code here

        # 递推公式和跳台阶问题一样，代码也相同
        # f(n) = f(n-1) + f(n-2)
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        a, b = 1, 2
        for i in range(3, number +1):
            a, b = b, a + b
        return b

print(Solution().rectCover(3))
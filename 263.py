"""
判断给定的数字是否为丑数，两个条件
（1）正数
（2）因子只有2，3，5
"""
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        while num > 1:
            if num % 2 ==0:
                num = num/2
            elif num % 3 ==0:
                num = num/3
            elif num % 5 ==0:
                num = num/5
            else:
                return False
                break
        if num == 1:
            return True
s=Solution()
print(s.isUgly(15))
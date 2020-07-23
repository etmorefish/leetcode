"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""
# [None, 1, 2, 3, 5, 8, 13, 21, 34, 55]
class Solution:
    def jumpFloor(self, number):
        if number == 1:
            return 1
        if number == 2:
            return 2
        if number > 2:
            ret = 0
            a = 1
            b = 2
            for i in range(0, number-2):
                ret = a+b
                a = b
                b = ret
            return ret

s = Solution()
print([s.jumpFloor(i) for i in range(10)])
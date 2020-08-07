"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

此类求 多少种可能性 的题目一般都有 递推性质 ，即 f(n)f(n) 和 f(n-1)f(n−1)…f(1)f(1) 之间是有联系的。

设跳上 nn 级台阶有 f(n)f(n) 种跳法。在所有跳法中，青蛙的最后一步只有两种情况： 跳上 11 级或 22 级台阶。
当为 11 级台阶： 剩 n-1n−1 个台阶，此情况共有 f(n-1)f(n−1) 种跳法；
当为 22 级台阶： 剩 n-2n−2 个台阶，此情况共有 f(n-2)f(n−2) 种跳法。
f(n)f(n) 为以上两种情况之和，即 f(n)=f(n-1)+f(n-2)f(n)=f(n−1)+f(n−2) ，以上递推性质为斐波那契数列。
本题可转化为 求斐波那契数列第 nn 项的值 ，与 面试题10- I. 斐波那契数列 等价，唯一的不同在于起始数字不同。
青蛙跳台阶问题： f(0)=1f(0)=1 , f(1)=1f(1)=1 , f(2)=2f(2)=2 ；
斐波那契数列问题： f(0)=0f(0)=0 , f(1)=1f(1)=1 , f(2)=1f(2)=1 。


"""
# [None, 1, 2, 3, 5, 8, 13, 21, 34, 55]
class Solution:
    def jumpFloor(self, number):
        if number == 1 or number == 0:
            return 1
        if number == 2:
            return 2
        if number > 2:
            ret = 0
            a = 1
            b = 2
            for i in range(number-2):
                ret = a+b
                a = b
                b = ret
            return ret

        # a, b = 1, 1
        # for _ in range(n):
        #     a, b = b, a+b
        # return a

s = Solution()
print([s.jumpFloor(i) for i in range(10)])
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级，......。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
1 2 3 4 5  n
1 2 4 8 16  2^(n-1)

f(n) = f(n-1)+f(n-2)+...+f(1)
f(n-1) = f(n-2)+...+f(1)
f(n) = 2f(n-1)  n>1
"""


class Solution:
    def jumpFloor(self, number):
        # return pow(2, number-1)
        if number == 1:
            return 1
        a = 1
        ret = 1
        if number >1:
            for i in range(2, number+1):
                ret = 2 * a
                a = ret
            return ret




s = Solution()
print([s.jumpFloor(i) for i in range(1,10)])

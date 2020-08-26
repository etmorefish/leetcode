'''
# 判断丑数
count = 0
def isUglyNumber(num):
    while num % 2 == 0:
        num //= 2
    while num % 3 == 0:
        num //= 3
    while num % 5 == 0:
        num //= 5
    if num == 1:
        return True
    else:
        return False
'''


class Solution:
    # 动态规划
    def nthUglyNumber(self, n: int) -> int:
        if n < 1:
            return None
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2:
                a += 1
            if dp[i] == n3:
                b += 1
            if dp[i] == n5:
                c += 1
        return dp[-1]

    def nthUglyNumber2(self, n):
        res = [1]
        a, b, c = 0, 0, 0
        tmp = 1
        while tmp < n:
            minval = min(res[a] *2, res[b]*3, res[c]*5)
            res.append(minval)
            tmp += 1
            if minval == res[a] *2:
                a += 1
            if minval == res[b] *3:
                b += 1
            if minval == res[c] * 5:
                c += 1
        return res[-1]

print(Solution().nthUglyNumber(10))
print(Solution().nthUglyNumber2(10))

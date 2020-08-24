class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            ret = 0
            a = 1
            b = 2
            for i in range(3, n+1):
                ret = a + b
                a = b
                b = ret
        return ret

    def climbStairs2(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a+b
        return a


print(Solution().climbStairs(20))
print(Solution().climbStairs2(2))

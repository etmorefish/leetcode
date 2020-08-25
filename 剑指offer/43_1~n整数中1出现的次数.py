
class Solution:
    def countDigitOne(self, n: int) -> int:
        res = 0
        def dfs(n):
            res = 0
            while(n):
                if n%10 == 1:
                    res += 1
                    n /= 10
            return res

        for i in range(1, n+1):
            res += dfs(i)
        return res


print(Solution().countDigitOne(824883294))
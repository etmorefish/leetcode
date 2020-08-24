class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':  # 基本情况，直接返回 0
            return 0
        if len(s) == 1:
            return 1

        dp = [0] * (len(s)+1)  # 构建 dp 数组
        dp[0] = 1  # 只有一个数时肯定为 1

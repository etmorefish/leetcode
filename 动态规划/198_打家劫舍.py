"""
给定一个数组，不能选择相邻的数，求如何选才能使总数最大
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+ nums[i])
        return dp[-1]
        # return max(dp)

print(Solution().rob([2,7,9,3,1]))
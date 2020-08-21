"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

时间复杂度 O(N^2) ： 遍历计算 dpdp 列表需 O(N)O(N)，计算每个 dp[i]dp[i] 需 O(N)O(N)。
空间复杂度 O(N) ： dpdp 列表占用线性大小额外空间。

"""

# Dynamic programming.
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):  # 8
            for j in range(i):
                if nums[j] < nums[i]:

                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxnum = nums[0]
        for i in range(1, len(nums)):
            if nums[i -1] >0:
                nums[i] += nums[i -1]
                print(nums[i])
            maxnum = max(nums[i], maxnum)
            print(maxnum)
        return maxnum

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
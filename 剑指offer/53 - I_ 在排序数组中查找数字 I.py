

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(nums, tar):
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            return l
        return helper(nums, target) - helper(nums, target-1)

    def search2(self, nums, target):
        tmp = nums.copy()
        tmp.reverse()
        if target in nums:
            a = nums.index(target)
            b = tmp.index(target)
            return len(nums[a:-b])
        return 0

    def search3(self, nums, target):
        if target in nums:
            ind = nums.index(target)
            i = 1



# print(Solution().search([5, 7, 7, 8, 8, 8, 10], 8))
# print(Solution().search2([5, 7, 7, 8, 8, 10], 8))
print(Solution().search3([0,1,1,1], 1))

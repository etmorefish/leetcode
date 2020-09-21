"""
283 移动零，在原地修改，双指针
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # slow = 0
        # for fast in range(len(nums)):
        #     if nums[fast] != 0:
        #         nums[slow], nums[fast] = nums[fast], nums[slow]
        #         slow += 1
        # return nums

        k = 0
        while 0 in nums:
            nums.remove(0)
            k += 1
        for i in range(k):
            nums.append(0)
        return nums


s = Solution()
print(s.moveZeroes([0, 1, 0, 3, 12]))

"""
283 移动零，在原地修改，双指针
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow],nums[fast]= nums[fast],nums[slow]
                slow += 1
        return nums

s=Solution()
print(s.moveZeroes([1]))
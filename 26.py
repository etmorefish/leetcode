#coding: utf-8 -*-
#从排序数组中删除重复项

"""
双指针，一个指针遍历数组，另一个指针点非重复项的个数
"""

class Solution:
    def removeDuplicates(self, nums):
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                nums[slow+1] = nums[fast]
                slow += 1
                fast += 1
        return nums

s=Solution()
print(s.removeDuplicates([1,1,2,2,4,6]))

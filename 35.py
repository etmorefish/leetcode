"""
35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
"""


class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)

    def binaryInsert(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def binaryInsert2(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def binaryInsert3(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                ans = mid
            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                ans = mid +1
                low = mid + 1
        return ans
    


s = Solution()
nums = [1, 3, 4, 6]
target = 0
# print(s.searchInsert(nums, target))
print(s.binaryInsert3(nums, target))

#两数之和

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map={}
        if not nums or len(nums)<2:
            return [-1,-1]
        for i in range(len(nums)):
            if target - nums[i] in map:
                return [i, map[target - nums[i]]]
            if nums[i] not in map:
                map[nums[i]] = i






# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#
#         hashmap = {}
#         for ind, num in enumerate(nums):
#             hashmap[num] = ind
#         for i, num in enumerate(nums):
#             j = hashmap.get(target - num)
#             if j is not None and i != j:
#                 return [i, j]
s=Solution()
print(s.twoSum([3,3],6))
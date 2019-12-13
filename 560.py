"""
连续子序列的和为k的个数
(1)暴力法：知道首尾位置，然后计算首尾位置之间的子序列的和
(2)用累加值组成hashmap
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        map={}
        num=0
        count=0
        for i in range(len(nums)):
            num = sum(nums[:(i+1)])
            if num == k:
                count += 1
            if num - k in map:
                count += map[num-k]
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        return count


s = Solution()
print(s.subarraySum([0,0,0,0,0,0,0,0,0,0],0))


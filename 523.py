class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map = {}
        num = 0
        count = 0
        map1={}
        for i in range(len(nums)):
            num = sum(nums[:(i + 1)])
            for i in range(1000):
                if num - i*k in map:
                    count += map[num - i*k]
                    continue
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        return count!=0
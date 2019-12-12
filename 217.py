class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map={}
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                return True
        return False
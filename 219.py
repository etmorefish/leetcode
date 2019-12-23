

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map={}
        count = 0
        for i,j in enumerate(nums):
            map[j] = i
        for i,j in enumerate(nums):
            if j in map and i != map[j]:
                if 0<(map[j] - i) <= k or 0 < i-map[j] <= k:
                    count += 1
        return count!=0


s=Solution()
print(s.containsNearbyDuplicate([0,1,2,3,4,0,0,7,8,9,10,11,12,0],1))


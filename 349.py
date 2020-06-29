"""
349 两个数组的交集,不用set
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map,result={},[]
        for i in nums1:
            map[i] = i
        for j in set(nums2):
            if j in map:
                result.append(j)
        return result


if __name__ == '__main__':
    l1 = [1, 2,3 ,4,5,7,8]
    l2 = [1,8, 12 , 21]
    res = Solution()
    r = res.intersection(l1, l2)
    print(r)
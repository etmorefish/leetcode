#coding: utf-8 -*-
"""
合并排列数组:注意特殊要求，在nums1上进行原地修改,原地修改需要覆盖之前的值，所以nums1从最后开始
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m== 0:
            for i in range(n):
                nums1[i] = nums2[i]

        while m>0 and n>0:
            if nums1[m-1]<nums2[n-1]:
                nums1[m+n-1]= nums2[n-1]
                n = n -1
            else:
                nums1[m+n-1] = nums1[m-1]
                m = m -1
        if n!=0:
            for i in range(n):
                nums1[i] = nums2[i]
        return nums1
s=Solution()
print(s.merge([2,0],1,[1],1))




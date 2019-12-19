# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 21:54:22 2019

@author: Administrator
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res

s=Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 21:42:17 2019

@author: Administrator
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x1 = 0  
        str_x = str(x)[::-1]
        x1 = int(str_x)
        return x1==x
    
s= Solution()         
print(s.isPalindrome(121))
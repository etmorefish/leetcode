# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Solution(object):
        def reverse(self,x):
            """
            :type x: int
            :rtype: int
            """
            a = 0
            if x > 0 :
                a = 1
            else:
                a = -1
            x = abs(x)
            str_x = str(x)[::-1]
            x = int(str_x)
            x = x*a
            if -2**31<x<2**31:
                return x
            else:
               return x
        
s= Solution()         
print(s.reverse(-120))
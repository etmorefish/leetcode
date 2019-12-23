# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Solution:
    def lengthOfLastWord(self, s):
            a = s.split()
            if len(a) == 0:
                return 0
            else:
                l = len(a)
                return len(a[l-1])
            


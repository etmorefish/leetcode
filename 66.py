# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 12:42:31 2019

@author: Administrator
"""

class Solution(object):
    def plusOne(self, digits):
        sums = 0
        for i in digits:
            sums = sums * 10 + i #10进制乘以10，进行累和；
        sums_str = str(sums + 1)
        return [int(j) for j in sums_str]

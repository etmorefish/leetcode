# -*- coding: utf-8 -*-
# @Time    : 19-8-2 下午3:57
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : 1_twosum.py
# @Software: PyCharm
from _ast import List


class Solution:
    def twoSum(self, nums, target):
        i = 0
        while i < len(nums):
            if i == len(nums) - 1:
                return "No solution here!"
            r = target - nums[i]
            # Can't use a num twice
            num = nums[i + 1:]
            if r in num:
                return [i, num.index(r) + i + 1]
            i = i + 1

if __name__ == '__main__':

    a = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    a.twoSum(nums,target)
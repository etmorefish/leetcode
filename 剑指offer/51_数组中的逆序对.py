'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。

 

示例 1:

输入: [7,5,6,4]
输出: 5

'''

from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        '''暴力破解
        代码超时
        '''

        res = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    res += 1
        return res


print(Solution().reversePairs([7, 5, 6, 4]))

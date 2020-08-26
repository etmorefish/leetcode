import functools
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 字典  空间复杂度高
        # cout = collections.Counter(nums)
        # for k,v in cout.items():
        #     if v == 1:
        #         return k

        # 异或
        # xor = 0
        # num1, num2 = 0, 0
        # for num in nums:
        #     xor ^= num
        # mask = 1
        # while xor & mask == 0:
        #     mask = mask << 1
        # for num in nums:
        #     if num & mask == 0:
        #         num1 ^= num
        #     else:
        #         num2 ^= num
        # return [num1, num2]

        ret = functools.reduce(lambda x, y: x ^ y, nums)
        # print(ret)
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]







print(Solution().singleNumber([4, 1, 2, 1, 2]))

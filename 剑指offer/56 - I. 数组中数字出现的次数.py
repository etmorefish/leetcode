'''
异或的性质
两个数字异或的结果a^b是将 a 和 b 的二进制每一位进行运算，得出的数字。 运算的逻辑是
如果同一位的数字相同则为 0，不同则为 1

异或的规律

任何数和本身异或则为 0

任何数和 0 异或是 本身

异或满足交换律。 即 a ^ b ^ c ，等价于 a ^ c ^ b


'''

from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        pass
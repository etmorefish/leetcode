"""
请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。
例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。

"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count('1')

        # 2.取余
        # count=0
        # while n!=0:
        #     a=n%2
        #     if a==1:count+=1
        #     n=n//2
        # return count

        # 位运算
        res = 0
        while n:
            print(n, bin(n))
            res += n & 1
            n >>= 1    # 右移运算符
        return res

s = Solution()
print(s.hammingWeight(60))
print(bin(60))
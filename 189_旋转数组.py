from typing import List


class Solution:
    # 思路一：插入
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums.pop())
        return nums

# 思路二：拼接
    def rotate2(self, nums, k):
        nums[:] = nums[-k:]+nums[:-k]
        return nums

# 思路三：三个翻转 ， 整体翻转， 前k翻转，后k翻转
    def r3(self, n, k):
        nums = n[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        return nums

# 思路四：模拟过程
    def r4(self, nums, k):
        n = len(nums)
        k %= n
        if k == 0:
            return nums
        start = 0
        tmp = nums[start]
        cnt = 0
        while cnt < n:
            pass



print(Solution().rotate([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
print(Solution().rotate2([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
print(Solution().r3([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

"""数组中出现次数超过一半的数字（摩尔投票法
本题常见解法如下：

哈希表统计法： 遍历数组 nums ，用 HashMap 统计各数字的数量，最终超过数组长度一半的数字则为众数。此方法时间和空间复杂度均为 O(N)O(N) 。
数组排序法： 将数组 nums 排序，由于众数的数量超过数组长度一半，因此 数组中点的元素 一定为众数。此方法时间复杂度 O(N log_2 N)O(Nlog
2
​
 N)。
摩尔投票法： 核心理念为 “正负抵消” ；时间和空间复杂度分别为 O(N)O(N) 和 O(1)O(1) ；是本题的最佳解法。
摩尔投票法本质思想就是利用 众数记为 +1 ，把其他数记为 -1 ，将它们全部加起来，显然和大于 0和抵消相减。


"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # 数组排序法
        # 需要的数字出现次数多于一半 那么排序后必定在中间
        # nums.sort()
        # return nums[len(nums)//2]

        # 摩尔投票法
        # votes = 0
        # for num in nums:
        #     if votes == 0:
        #         x = num
        #     if num == x:
        #         votes += 1
        #     else:
        #         votes -= 1
        # return x

        # hash
        s = {}
        for num in nums:
            if num in s:
                s[num] += 1
            else:
                s.update({num: 1})
        return max(s.items(), key=lambda x:x[1])[0]




print(Solution().majorityElement([1, 2, 3, 2, 5, 2, 2, 2, 1]))
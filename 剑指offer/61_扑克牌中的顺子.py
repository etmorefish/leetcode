from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:

        # 方法一： 集合 Set + 遍历
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0:
                continue    # 跳过大小王
            ma = max(ma, num)   # 最大牌
            mi = min(mi, num)   # 最小牌
            if num in repeat:
                return False    # 若有重复，提前返回 false
            repeat.add(num)     # 添加牌至 Set
        return ma-mi < 5    # 最大牌 - 最小牌 < 5 则可构成顺子


        # 方法二：排序 + 遍历     数组排序使用 O(NlogN) 时间。

        joker = 0
        nums.sort()  # 数组排序
        for i in range(4):
            if nums[i] == 0:
                joker += 1  # 统计大小王数量
            elif nums[i] == nums[i + 1]:
                return False  # 若有重复，提前返回 false
        return nums[4] - nums[joker] < 5  # 最大牌 - 最小牌 < 5 则可构成顺子


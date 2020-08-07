"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

"""

class Solution:
    def minArray(self, numbers) -> int:
        # 排序数组的查找问题首先考虑使用 二分法 解决，其可将遍历法的 线性级别 时间复杂度降低至 对数级别

        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]:
                i = m +1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                j -= 1
        return numbers[i]

s = Solution()
print(s.minArray([3,4,5,6,7,1,2]))
print(s.minArray([1,2,3,4,5,]))
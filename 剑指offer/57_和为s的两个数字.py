from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 哈希表
        # hashmap = {}
        # for i, v in enumerate(nums):
        #     hashmap[v] = i
        # for i, v in enumerate(nums):
        #     res = hashmap.get(target - v)
        #     if res and res != i:
        #         return [v, nums[res]]

        # 对碰双指针  最优
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return [nums[i], nums[j]]
        return []

        # 二分法
        # if nums[0] > target:
        #     return
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     mid = l + (r - l) // 2
        #     tmp = target - nums[l]
        #     if nums[mid] == tmp:
        #         return [tmp, nums[l]]
        #     elif nums[mid] > tmp:
        #         r = mid -1
        #     else:
        #         l = mid +1
        #     l += 1
        # return []



print(Solution().twoSum([2,6, 7, 11, 15], 26))

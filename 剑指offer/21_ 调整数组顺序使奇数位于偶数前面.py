class Solution:
    # def exchange(self, nums: List[int]) -> List[int]:
    #     ret1 = []
    #     ret2 = []
    #     for i in nums:
    #         if i % 2 == 1:
    #             ret1.append(i)
    #         else:
    #             ret2.append(i)
    #     return ret1+ret2

    # 双指针
    def exchange(nums):
        pre, end = 0, len(nums)-1
        while pre < end:
            if nums[pre] % 2 == 1 and nums[end] % 2 == 1:
                pre += 1
            elif nums[pre] % 2 == 0 and nums[end] % 2 == 0:
                end -= 1
            elif nums[pre] % 2 == 1 and nums[end] % 2 == 0:
                pre += 1
                end -= 1
            elif nums[pre] % 2 == 0 and nums[end] % 2 == 1:
                nums[pre], nums[end] = nums[end], nums[pre]
                pre += 1
                end -= 1
        return nums


# print(Solution.exchange([1,2,3,4,4,4,5,6,7,8,9]))
print(Solution.exchange([11, 9, 3, 7, 16, 4, 2, 0]))

# 11  9 3 4 7 16  2 0

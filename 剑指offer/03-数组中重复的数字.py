def duplicate(nums: list) -> int:
    for i, num in enumerate(nums):
        while i != num:
            if num == nums[num]:
                return True, num
            else:
                nums[i], nums[num] = nums[num], nums[i]
                num = nums[i]
        return False, None


# 排序做法  O(nlogn)


def findRepeatNumber1(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    pre = nums[0]
    for index in range(1, len(nums)):
        if pre == nums[index]:
            return pre
        pre = nums[index]


# 哈希表  O(n)


def findRepeatNumber2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 0
        else:
            return i




class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1

# 下表定位
def findRepeatNumber3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(len(nums)):
        while nums[i] != i:
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

    return None


a = [1, 2, 3, 4, 4, 5, 5, 6]
# b = [1, 2, 3, 4, 5, 6]
# print(duplicate(a))
print(findRepeatNumber2(a))
s= Solution()
s.findRepeatNumber(a)
print(s.findRepeatNumber(a))

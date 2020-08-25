from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # arr.sort()
        # return arr[:k]

        # 快排
        def partition(arr, left, right):
            tmp = arr[left]
            while left < right:
                while left < right and arr[right] >= tmp:
                    right -= 1
                arr[left] = arr[right]
                while left < right and arr[left] <= tmp:
                    left += 1
                arr[right] = arr[left]
            arr[left] = tmp
            return left

        def quick_sort(arr, left, right):
            if left < right:
                mid = partition(arr, left, right)
                quick_sort(arr, left, mid - 1)
                quick_sort(arr, mid + 1, right)
            return arr

        res = quick_sort(arr, 0, len(arr) - 1)
        return res[:k]


print(Solution().getLeastNumbers([0, 0, 1, 2, 4, 2, 2, 3, 1, 4], 5))

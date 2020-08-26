import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 切片暴力法
        # res = []
        # for i in range(len(nums) - k +1):
        #     tmp = nums[i:i+k]
        #     res.append(max(tmp))
        # return res

        # 单调队列法。
        # 维护一个队列。保持队列是单调递减，即加入时把前面比其小的数pop掉。
        res, q = [], collections.deque()
        for i in range(1 - k, len(nums) - k + 1):
            if i > 0 and q[0] < i:
                q.popleft()
            while q and nums[i + k - 1] > nums[q[-1]]:
                q.pop()
            q.append(i + k - 1)
            if i >= 0:
                res.append(nums[q[0]])
        return res

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        # init
        deque = collections.deque()
        res = []
        n = len(nums)
        # 设滑动边界, i为左边界, j为有边界, 打包形成滑动窗口, 然后遍历
        # Python 通过 zip(range(), range()) 可实现滑动窗口的左右边界 i, j 同时遍历。
        for i, j in zip(range(1 - k, 1 - k + n), range(0, n)):
            # 制定规则, 始终奉行在deque[0]存储最大值
            # 先看deque队首, i=0时因前面无值没有值可以滑出（所以从i=1开始，此时num[0]就是滑出值）
            # 同时当nums[i-1]滑出窗口时, 即判定条件是deque[0] == nums[i-1], 将队首取出
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()
            # 然后继续判定划入窗口的值是补入队尾还是队首
            # deque不为空时便有队尾，同时满足队尾deque[-1]<num[j]时将nums[j]补在队首
            # 否则直接补在队尾
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            # res的补入原则
            if i >= 0:
                res.append(deque[0])
        # 返回值
        return res


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))

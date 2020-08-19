'''
例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
                    你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

'''

class Solution:
    def dailyTemperatures(self, T):
        res = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:  # 栈不为空 && 栈顶温度小于当前温度
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
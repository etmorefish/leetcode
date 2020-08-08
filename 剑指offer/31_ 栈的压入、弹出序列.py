# pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack, index = [], 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1
        return not stack
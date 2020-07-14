# 1249. 移除无效的括号

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = []
        count = []
        for i in range(len(s)):
            if s[i] == '(':
                # stack.append(("(", i))
                stack.append(i)
            elif s[i] == ')' and stack != []:
                stack.pop()
            elif s[i] == ')' and stack == []:
                # remove.append((')', i))
                remove.append(i)
        # for i in stack+remove:
        #     s = s[:i] + ' ' + s[i + 1:]
        #     print(s.replace(' ', ''))
        count = stack+remove
        count.sort()
        count.reverse()
        # print(count)
        sl = list(s)
        for i in count:
            sl.pop(i)

        # print(''.join(sl))
        return ''.join(sl)



if __name__ == '__main__':
    s = "l)ee(t(c)o)de)"
    s1 = ')))(((('
    a = Solution()
    a.minRemoveToMakeValid(s1)

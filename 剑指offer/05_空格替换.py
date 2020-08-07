class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        # return s.replace(' ', '%20')
        a = []
        for i in s:
            if i == ' ':
                a.append('%')
                a.append('2')
                a.append('0')
            else:
                a.append(i)
        return ''.join(a)
s = Solution()
print(s.replaceSpace('We Are Happy'))
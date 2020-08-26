class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # 切片    效率最高。
        n = n % len(s)
        # return s[n:] + s[:n]

        # “列表遍历拼接”
        res = []
        # for i in range(n, len(s)):
        #     res.append(s[i])
        # for i in range(n):
        #     res.append(s[i])
        for i in range(n, n + len(s)):
            res.append(s[i % len(s)])
        return ''.join(res)

        '''字符串遍历拼接   
        每轮遍历拼接字符时，都需要新建一个字符串；因此，系统 需申请 NN 次内存 ，数据量较大时效率低下。
        '''
        res = ""
        for i in range(n, len(s)):
            res += s[i]
        for i in range(n):
            res += s[i]
        return res


print(Solution().reverseLeftWords("agoodexample", 5))

class Solution:
    # 哈希表
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = True
            else:
                dic[c] = False
        for c in s:
            if dic[c]:
                return c
        return ' '

    # 有序哈希表
    def firstUniqChar2(self, s):
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = True
            else:
                dic[c] = False
        for k,v in dic.items():
            if v:
                return k
        return ' '

print(Solution().firstUniqChar('qqwduyschwas'))
print(Solution().firstUniqChar2('qqwduyschwas'))

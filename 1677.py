"""
面试题 16.11. 跳水板
你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。
你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

返回的长度需要从小到大排列。

"""

class Solution:
    """
    shorter*k  -> 最短,
    longer*k +1   -> 最长,
    longer-shorter   -> 差值
    """
    def divingBoard( shorter: int, longer: int, k: int):
        if k == 0:
            return []
        elif shorter == longer:
            return[shorter*k]
        else:
            return list(range(shorter*k, longer*k +1, longer-shorter))

shorter = 1
longer = 9
k = 6
s = Solution
print(s.divingBoard(shorter, longer, k))

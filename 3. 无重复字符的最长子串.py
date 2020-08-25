# 滑动窗口

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = 0
        mark = []
        for end in range(len(s)):
            while s[end] in mark:
                mark.remove(s[start])
                start += 1
            max_len = max(max_len, end - start + 1)
            mark.append(s[end])
        return max_len
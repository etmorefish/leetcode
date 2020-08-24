# 滑动窗口

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mark = []
        start = 0
        max_len = 0
        for end in range(len(s)):
            while s[end] in mark:
                mark.remove(s[start])
                start += 1
            mark.append(s[end])
            max_len = max(max_len, end - start + 1)


        return max_len


print(Solution().lengthOfLongestSubstring("pwwop"))

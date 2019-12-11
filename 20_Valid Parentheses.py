# -*- coding: utf-8 -*-
# @Time    : 19-7-29 下午3:11
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : 20_Valid Parentheses.py
# @Software: PyCharm

class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return True
    def isValid2(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
            else:
                stack.append(char)
            return not stack

if __name__ == '__main__':
    a = Solution()
    a.isValid2("()[]{}")

'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

class Solution(object):
    def middleNode(self, head):
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) / 2]

class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow




示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


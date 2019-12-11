# -*- coding: utf-8 -*-
# @Time    : 19-12-7 下午9:25
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : #83.py
# @Software: PyCharm
'''
如果当前节点和下一个节点的值相同，则返回第二个节点
在每个递归中将下一个递归结果连接到当前节点
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head:
            head.next = self.deleteDuplicates(head.next)
            return head.next if head.next and head.val == head.next.val else head


class Solution2(object):
    def deleteDuplicates(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not (head and head.next):
			return head
		i,j = head,head
		while j:
			# 如果i不等于j，则i前进一位，然后将j的值赋给i
			# 请配合动画演示理解
			if i.val!=j.val:
				i = i.next
				i.val = j.val
			# 不管i是否等于j，j每次都前进一位
			j = j.next
		i.next = None
		return head


class Solution3:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans = head
        while head != None:
            if head.next != None and head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        return ans


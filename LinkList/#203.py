# -*- coding: utf-8 -*-
# @Time    : 19-12-7 下午10:42
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : #203.py
# @Software: PyCharm


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head != None and head.val == val:
            head = head.next
        if head == None:
            return None
        else:
            node =  head
            while node.next != None:
                if node.next.val == val:
                    node.next == node.next.next
                else:
                    node = node.next
        return head
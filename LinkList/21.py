# -*- coding: utf-8 -*-
# @Time    : 19-12-4 下午7:39
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : #21.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2

"""

class Solution:
    # 将输入列表转换为链表
    def initList(self, data):
        # 判空
        if len(data) == 0:
            return
        else:
            # 创建头结点
            self.head = ListNode(data[0])
            r = self.head
            p = self.head
            # 逐个为 data 内的数据创建结点, 建立链表
            for i in data[1:]:
                node = ListNode(i)
                p.next = node
                p = p.next
            return r

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_list = []
        cur = l1
        while cur is not None:
            result_list.append(cur.val)
            cur = cur.next
        cur = l2
        while cur is not None:
            result_list.append(cur.val)
            cur = cur.next
        sorted_list = sorted(result_list)
        if len(sorted_list) == 0:
            return
        else:
            node = ListNode(sorted_list[0])
            cur = node
            for i in range(1, len(sorted_list)):
                cur.next = ListNode(sorted_list[i])
                cur = cur.next
        # 显示结果用
        cur = node
        display = []
        while cur is not None:
            display.append(cur.val)
            cur = cur.next
        return display



if __name__ == "__main__":
    test = Solution()
    data1 = [1, 3, 2]
    data2 = [6, 5, 4]
    l1 = test.initList(data1)
    l2 = test.initList(data2)
    result = test.mergeTwoLists(l1, l2)
    print(result)




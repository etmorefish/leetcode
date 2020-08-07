# -*- coding:utf-8 -*-
'''
题目：如果一个链表中包含环，如何找出环的入口节点？例如，在如图所示的链表中，环的入口节点是节点3
         _____<_____
        |           |
1-->2-->3-->4-->5-->6
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# class Solution:
#     def EntryNodeOfLoop(self, pHead):
#         # write code here
#         fast = pHead
#         slow = pHead
#         while True:
#             if fast and fast.next:
#                 fast = fast.next.next
#                 slow = slow.next
#             else:
#                 return None
#             if fast == slow:
#                 fast = pHead
#                 break
#         while fast != slow:
#             fast = fast.next
#             slow = slow.next
#         return fast


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        # 遍历链表，环的存在，遍历遇见的第一个重复的即为入口节点
        cur = pHead
        ret = []
        while cur:
            if cur in ret:
                return cur
            else:
                ret.append(cur)
            cur = cur.next


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

print(Solution().EntryNodeOfLoop(node1).val)

'''
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        dummyHead = ListNode(0)
        dummyHead.next = head
        pre, cur = dummyHead, head
        while cur:  # 当前节点存在
            while cur.next and cur.val == cur.next.val:  # 下一个节点存在，且与当前节点值重复
                cur = cur.next  # 当前节点后移
            if pre.next == cur:  # 前一个节点的后节点为当前节点，意味着当前节点未移动，且后一个节点不重复
                pre = pre.next  # 前一个节点后移
            else:  # 前一个节点的后节点不为当前节点，意味着当前节点移动，且后一个节点重复
                pre.next = cur.next  # 跳过重复部分
            cur = cur.next  # 当前节点后移
        return dummyHead.next

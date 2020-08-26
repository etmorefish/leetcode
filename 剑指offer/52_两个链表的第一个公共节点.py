"""
解题思路：
我们使用两个指针 node1，node2 分别指向两个链表 headA，headB 的头结点，
然后同时分别逐结点遍历，当 node1 到达链表 headA 的末尾时，
重新定位到链表 headB 的头结点；当 node2 到达链表 headB 的末尾时，
重新定位到链表 headA 的头结点。
这样，当它们相遇时，所指向的结点就是第一个公共结点。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        ha, hb = headA, headB
        while ha != hb:
            # if ha:
            #     ha = ha.next
            # else:
            #     ha = headB
            # if hb:
            #     hb = hb.next
            # else:
            #     hb = headA
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha
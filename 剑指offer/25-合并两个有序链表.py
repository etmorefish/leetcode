# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # l = []
        # while l1:
        #     l.append(l1.val)
        #     l1 = l1.next
        # while l2:
        #     l.append(l2.val)
        #     l2 = l2.next
        # l.sort()

        # head = ListNode(0)
        # curr = head
        # for i in l:
        #     node = ListNode(i)
        #     curr.next = node
        #     curr = curr.next
        # return head.next

        # 递归
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <=  l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
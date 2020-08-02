# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = ListNode(None)

        cur = p
        tmp = 0
        while l1 or l2 or tmp:
            tmp += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(tmp % 10)
            p = p.next
            tmp //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return cur.next
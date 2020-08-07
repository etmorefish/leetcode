# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pReverseHead = None
        pNode = pHead
        pPrev = None

        while pNode:
            pNext = pNode.next
            if pNext == None:  # 只有一个节点
                pReverseHead = pNode
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return pReverseHead


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 申请两个节点，pre和 cur，pre指向None
        pre = None
        cur = head
        # 遍历链表，while循环里面的内容其实可以写成一行
        # 这里只做演示，就不搞那么骚气的写法了
        while cur:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        if not head:
            return head
        # 把head中的值加入栈里
        while head:
            stack.append(head.val)
            head = head.next
        # 取最后加入的一个，即链表尾作为新的链表头
        cur = ListNode(stack.pop())
        # 记住头部索引
        res = cur
        # 依次给新链表赋值
        while stack:
            res.next = ListNode(stack.pop())
            res = res.next
        # 返回新链表头部
        return cur

# 输入一个链表，输出该链表中倒数第k个结点。
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        # k如果比我们的链表长度大，然回None、
        # k如果小于链表长度，我们定义两个变量，间隔为k
        firstPoint = head
        sencondPoint = head
        for i in range(k):
            if firstPoint == None:
                return None
            firstPoint = firstPoint.next
        
        while firstPoint:
            sencondPoint = sencondPoint.next
            firstPoint = firstPoint.next
        return sencondPoint
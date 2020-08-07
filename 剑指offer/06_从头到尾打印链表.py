"""
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printNode(node):
    while node:
        print(node.val, end='->')
        node = node.next


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        ret = []
        pTmp = listNode
        while pTmp:
            ret.insert(0, pTmp.val)
            # ret.append(pTmp.val)
            pTmp = pTmp.next
        return ret  
        # return ret[::-1]

# 递归
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head is None:
            return []
        res = self.reversePrint(head.next)
        res.append(head.val)
        return res




l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = None

printNode(l1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
特例处理： 当应删除头节点 head 时，直接返回 head.next 即可。
初始化： pre = head , cur = head.next 。
定位节点： 当 cur 为空 或 cur 节点值等于 val 时跳出。
保存当前节点索引，即 pre = cur 。
遍历下一节点，即 cur = cur.next 。
删除节点： 若 cur 指向某节点，则执行 pre.next = cur.next 。（若 cur 指向 nullnull ，代表链表中不包含值为 val 的节点。
返回值： 返回链表头部节点 head 即可。
"""
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:

        if head.val == val: 
            return head.next
        pre, cur = head, head.next
        while cur.val != val:
            pre, cur = cur, cur.next
        if cur: 
            pre.next = cur.next
        return head
# -*- coding: utf-8 -*-
# @Time    : 19-12-5 下午3:25
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : #2.py
# @Software: PyCharm


class Node(object):
    """单链表的结点"""

    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None

class Solution:
    def __init__(self):
        self._head = None

    def add(self, item):
        """向链表头部添加元素"""
        node = Node(item)
        # 新结点指针指向原头部结点
        node.next = self._head
        # 头部结点指针修改为新结点
        self._head = node

    def items(self):
        """遍历链表"""
        # 获取head指针
        cur = self._head
        # 循环遍历
        while cur is not None:
            # 返回生成器
            yield cur.item
            # 指针下移
            cur = cur.next

    def addTwoNumbers(self, l1, l2):
        pass

if __name__ == '__main__':

    s = Solution()
    for i in [2, 4, 3]:
        s.add(i)
    print(list(s.items()))
    a = ''.join('%s'%i for i in list(s.items()))
    print(a, type(a))

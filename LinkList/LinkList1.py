# -*- coding: utf-8 -*-
# @Time    : 19-12-4 下午5:55
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : LinkList1.py
# @Software: PyCharm


class Node(object):
    """单链表的结点"""

    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None

class SingleLinkList(object):
    """单链表"""

    def __init__(self):
        self._head = None

if __name__ == '__main__':
    # 创建链表
    link_list = SingleLinkList()
    # 创建结点
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    # 将结点添加到链表
    link_list._head = node1
    # 将第一个结点的next指针指向下一结点
    node1.next = node2
    node2.next = node3

    # 访问链表
    print(link_list._head.item)  # 访问第一个结点数据
    print(link_list._head.next.item)  # 访问第二个结点数据
    print(link_list._head.next.next.item)  # 访问第二个结点数据
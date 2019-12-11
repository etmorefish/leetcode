# -*- coding: utf-8 -*-
# @Time    : 19-12-7 下午9:56
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : #141.py
# @Software: PyCharm
# 哈希表
'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2

示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
'''
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        st = set()
        while p:
            if p in st:
                return True
            st.add(p)
            p = p.next
        return False
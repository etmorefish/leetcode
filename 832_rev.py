# -*- coding: utf-8 -*-
# @Time    : 19-7-29 下午4:31
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : 832_rev.py
# @Software: PyCharm


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for l in A:
            for i,v in enumerate(l[::-1]):
                if v == 1:
                    l.i[i]

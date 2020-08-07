# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        res = [root]
        ret = []
        while res:
            tmp = res[0]
            ret.append(tmp.val)    
            if tmp.left:
                res.append(tmp.left)
            if tmp.right:
                res.append(tmp.right)
            del res[0]
        return ret
# Definition for a binary tree node.
"""
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
    3
   / \
  9  20
    /  \
   15   7
"""

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        # 左子树在前序列表中的子列表 9
        left_pre = preorder[1:index+1]
        # 左子树在中序列表中的子列表 9
        left_in = inorder[:index]
        # 右子树在前序列表中的子列表 20 15 7
        right_pre = preorder[index+1:]
        # 右子树在中序列表中的子列表 15 20 7
        right_in = inorder[index+1:] 

        # 遍历创建子树
        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)

        return root



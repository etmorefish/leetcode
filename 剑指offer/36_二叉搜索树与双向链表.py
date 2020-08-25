"""面试题36. 二叉搜索树与双向链表（中序遍历） 左中右

"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        # 打印中序遍历
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)  # 递归左子树
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:
                self.head = cur
            self.pre = cur
            # print(root.val)  # 根
            dfs(cur.right)  # 右

        if not root:
            return
        self.pre = None
        dfs(root)
        # 将尾节点和头节点连接起来
        self.pre.right, self.head.left = self.head, self.pre
        return self.head

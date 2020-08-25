"""37. 序列化二叉树（层序遍历 BFS
序列化 serialize ：
借助队列，对二叉树做层序遍历，并将越过叶节点的 nullnull 也打印出来。
算法流程：
特例处理： 若 rootroot 为空，则直接返回空列表 "[]" ；
初始化： 队列 queuequeue （包含根节点 rootroot ）；序列化列表 resres ；
层序遍历： 当 queuequeue 为空时跳出；
节点出队，记为 nodenode ；
若 nodenode 不为空：① 打印字符串 node.valnode.val ，② 将左、右子节点加入 queuequeue ；
否则（若 nodenode 为空）：打印字符串 "null" ；
返回值： 拼接列表（用 ',' 隔开，首尾添加中括号）。

反序列化 deserialize ：
基于本文一开始分析的 “ nodenode , node.leftnode.left , node.rightnode.right ” 在序列化列表中的位置关系，可实现反序列化。

利用队列按层构建二叉树，借助一个指针 ii 指向节点 nodenode 的左、右子节点，每构建一个 nodenode 的左、右子节点，指针 ii 就向右移动 11 位。

算法流程：
特例处理： 若 datadata 为空，直接返回 nullnull ；
初始化： 序列化列表 valsvals （先去掉首尾中括号，再用逗号隔开），指针 i = 1i=1 ，根节点 rootroot （值为 vals[0]vals[0] ），队列 queuequeue（包含 rootroot ）；
按层构建： 当 queuequeue 为空时跳出；
节点出队，记为 nodenode ；
构建 nodenode 的左子节点：node.leftnode.left 的值为 vals[i]vals[i] ，并将 node.leftnode.left 入队；
执行 i+=1i+=1 ；
构建 nodenode 的右子节点：node.leftnode.left 的值为 vals[i]vals[i] ，并将 node.leftnode.left 入队；
执行 i+=1i+=1 ；
返回值： 返回根节点 rootroot 即可。

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('null')
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != 'null':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != 'null':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
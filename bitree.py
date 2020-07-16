from collections import deque

# 节点定义
class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.rchild = None
        self.lchild = None

a = BiTreeNode('A')
b = BiTreeNode('B')
c = BiTreeNode('C')
d = BiTreeNode('D')
e = BiTreeNode('E')
f = BiTreeNode('F')
g = BiTreeNode('G')

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e

# 前序遍历  E,A,C,B,D,G,F
def pre_order(root):
    if root:
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)

# 中序遍历  A,B,C,D,E,G,F
def mid_order(root):
    if root:
        mid_order(root.lchild)
        print(root.data, end=',')
        mid_order(root.rchild)

# 后序遍历  B,D,C,A,F,G,E
def bck_order(root):
    if root:
        bck_order(root.lchild)
        bck_order(root.rchild)
        print(root.data, end=',')

# 层次遍历  E,A,G,C,F,B,D
def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        print(node.data, end=',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)
level_order(root)
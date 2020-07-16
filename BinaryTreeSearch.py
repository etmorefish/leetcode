
# 节点定义
class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.rchild = None
        self.lchild = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None

    # def insert(self, node, val):
    #     if not
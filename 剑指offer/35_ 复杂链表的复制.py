


"""
# Definition for a Node.
"""
import collections


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # return copy.deepcopy(head)

# """
# 算法：深度优先搜索
# 从头结点 head 开始拷贝；
# 由于一个结点可能被多个指针指到，因此如果该结点已被拷贝，则不需要重复拷贝；
# 如果还没拷贝该结点，则创建一个新的结点进行拷贝，并将拷贝过的结点保存在哈希表中；
# 使用递归拷贝所有的 next 结点，再递归拷贝所有的 random 结点。
# """
        def dfs(head):
            if not head: return None
            if head in visited:
                return visited[head]
            # 创建新结点
            copy = Node(head.val, None, None)
            visited[head] = copy
            copy.next = dfs(head.next)
            copy.random = dfs(head.random)
            return copy
        visited = {}
        return dfs(head)

'''
算法：广度优先搜索
创建哈希表保存已拷贝结点，格式 {原结点：拷贝结点}
创建队列，并将头结点入队；
当队列不为空时，弹出一个结点，如果该结点的 next 结点未被拷贝过，则拷贝 next 结点并加入队列；同理，如果该结点的 random 结点未被拷贝过，则拷贝 random 结点并加入队列；

'''
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}
    
        def bfs(head):
            if not head: return head
            clone = Node(head.val, None, None) # 创建新结点
            queue = collections.deque()
            queue.append(head)
            visited[head] = clone
            while queue:
                tmp = queue.pop()
                if tmp.next and tmp.next not in visited:
                    visited[tmp.next] = Node(tmp.next.val, [], [])
                    queue.append(tmp.next)  
                if tmp.random and tmp.random not in visited:
                    visited[tmp.random] = Node(tmp.random.val, [], [])
                    queue.append(tmp.random)
                visited[tmp].next = visited.get(tmp.next)
                visited[tmp].random = visited.get(tmp.random)
            return clone
        return bfs(head)


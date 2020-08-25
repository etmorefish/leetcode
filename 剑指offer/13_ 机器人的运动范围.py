""" 机器人的运动范围（ DFS / BFS
本题与 矩阵中的路径 类似

结论： 根据可达解的结构，易推出机器人可 仅通过向右和向下移动，访问所有可达解

方法一：深度优先遍历 DFS
深度优先搜索： 可以理解为暴力法模拟机器人在矩阵中的所有路径。DFS 通过递归，先朝一个方向搜到底，再回溯至上个节点，沿另一个方向搜索，以此类推。
剪枝： 在搜索中，遇到数位和超出目标值、此元素已访问，则应立即返回，称之为 可行性剪枝 。
算法解析：
递归参数： 当前元素在矩阵中的行列索引 i 和 j ，两者的数位和 si, sj 。
终止条件： 当 ① 行列索引越界 或 ② 数位和超出目标值 k 或 ③ 当前元素已访问过 时，返回 00 ，代表不计入可达解。
递推工作：
标记当前单元格 ：将索引 (i, j) 存入 Set visited 中，代表此单元格已被访问过。
搜索下一单元格： 计算当前元素的 下、右 两个方向元素的数位和，并开启下层递归 。
回溯返回值： 返回 1 + 右方搜索的可达解总数 + 下方搜索的可达解总数，代表从本单元格递归搜索的可达解总数。

作者：jyd
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
# 方法：广度优先搜索

# 数位之和计算：
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def sums(x):
            s = 0
            while x != 0:
                s += x % 10
                x //= 10
            return s

        path = []
        s = set()
        path.append((0, 0))
        while path:
            x, y = path.pop()
            if (x, y) not in s and 0 <= x < m and 0 <= y < n and sums(x) + sums(y) <= k:
                s.add((x, y))
                for nx, ny in [(x + 1, y), (x, y + 1)]:    # 通过向右和向下移动，访问所有可达解
                    path.append((nx, ny))
        # print(path)
        # print(s)
        return len(s)


print(Solution().movingCount(2, 3, 1))

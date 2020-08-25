
'''
1.把n-1个盘子从a经过c移动到b
2.把第n个圆盘从a移动到c
3.把你n-1个盘子从b经过a移动到c
'''


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)   # 从a 经过 c 移动到 b
        print('moving from to %s to %s' % (a, c))  # a移动到c
        hanoi(n-1, b, a, c)   # 从b 经过 a 移动到 c
    print(c)


hanoi(2, 'A', 'B', 'C')

# class Solution:
#     def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
#         n = len(A)
#         self.move(n, A, B, C)
#     # 定义move 函数移动汉诺塔
#     def move(self,n, A, B, C):
#         if n == 1:
#             C.append(A[-1])
#             A.pop()
#             return
#         else:
#             self.move(n-1, A, C, B)  # 将A上面n-1个通过C移到B
#             C.append(A[-1])          # 将A最后一个移到C
#             A.pop()                  # 这时，A空了
#             self.move(n-1,B, A, C)   # 将B上面n-1个通过空的A移到C


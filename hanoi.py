
'''
1.把n-1个盘子从a经过c移动到b
2.把第n个圆盘从a移动到c
3.把你n-1个盘子从b经过a移动到c
'''


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print('moving from to %s to %s' % (a, c))
        hanoi(n-1, b, a, c)


hanoi(3, 'A', 'B', 'C')

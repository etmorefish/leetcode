"""
一一个小小偷在某个商店发现有n个商品,第i个商品价值v i 元,重w i 千克。他希望
拿走走的价值尽量量高高,但他的背包最多只能容纳W千克的东⻄西。他应该拿走走哪些
商品?

0-1背包:对于一一个商品,小小偷要么把它完整拿走走,要么留留下。不不能只拿走走
一一部分,或把一一个商品拿走走多次。(商品为金金金条)

分数背包:对于一一个商品,小小偷可以拿走走其中任意一一部分。(商品为金金金砂)

举例例:
商品1:v 1 =60 w 1 =10
商品2:v 2 =100 w 2 =20
商品3:v 3 =120 w 3 =30
背包容量量:W=50

对于0-1背包和分数背
包,贪心心算法是否都能
得到最优解?为什什么?
"""

# 分数背包
goods = [(60, 10), (100, 20), (120, 30)]
goods.sort(key=lambda x: x[0] / x[1], reverse=True)


def fractional_backpack(goods, w):
    m = [0 for _ in range(len(goods))]
    total_v = 0
    for i, (price, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            total_v += price
            w -= weight
        else:
            m[i] = w / weight
            total_v += price * m[i]
            w = 0
            break
    return m, total_v


print(fractional_backpack(goods, 50))

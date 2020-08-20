"""
有n个非非负整数,将其按照字符串串拼接的方方式拼接为一一个整数。
如何拼接可以使得得到的整数最大大?
例例:32,94,128,1286,6,71可以拼接除的最大大整数为
94716321286128

x+y 1281286
y+x 1286128

"""
from functools import cmp_to_key

li = [32, 94, 128, 1286, 6, 71]


def xy_cmp(x, y):
    if x + y < y + x:
        return 1
    elif x + y > y + x:
        return -1
    else:
        return 0


def numer_join(li):
    li = list(map(str, li))
    print(li)
    li.sort(key=cmp_to_key(xy_cmp))
    print(li)
    return ''.join(li)


print(numer_join(li))

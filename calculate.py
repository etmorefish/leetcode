"""解题思路
(a+b)*c-d/e
遍历将数字和运算符分别入栈
得到 data = [a, b, c, d, e]
    opt = [(, +, ), *, -, /]
取出opt栈顶的元素

"""
import re


class Solution:
    def calculate(self, s: str) -> int:
        pass


a = '(2+3.1)*4-8.22/2'
data = re.findall("\d+\.?\d+|\d+", a)
opt = re.findall("[-()\+\*\/]", a)
# data = ['2', '3.1', '4', '8.2', '2']
# opt = ['(', '+', ')', '*', '-', '/']
print('data: ', data, '\n', 'opt: ', opt)
power = {'(': 3, ')': 3,
         '*': 2, '/': 2,
         '+': 1, '-': 1}
ret = 0
i = 0
lo = len(opt)
ld = len(data)

if power[opt[-1]] >= power[opt[-2]]:
    if opt[-1] == '/':
        ret = float(data[-2]) / float(data[-1])
        print(ret)
        data = data[:-2]
        data.append(str(ret))
        opt.pop()
    elif opt[-1] == '*':
        ret = float(data[-2]) * float(data[-1])
        print(ret)
        data = data[:-2]
        data.append(str(ret))
        opt.pop()
    else:
        pass


if power[opt[-1]] < power[opt[-2]]:
    pass




print(data)
print(opt)
print(ret)
# while i < len(opt):
#     if
'''
re.findall("(\d+(\.\d+)?)", a)
Out[58]: [('2', ''), ('3.1', '.1'), ('4', ''), ('8.2', '.2'), ('2', '')]

re.findall("\d+\.?\d+?|\d+", a)
Out[67]: ['2', '3.1', '4', '8.2', '2']

re.findall("[-()\+\*\/]", a)
Out[95]: 
'''

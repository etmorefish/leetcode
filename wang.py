def f1(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum


print(f1(100))


def f2(n):
    pass


def f3():
    nums = [1, 5, 2, 8, 3]
    length = len(nums)
    for i in range(length - 1):
        exchange = False
        for j in range(length - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                exchange = True
        if not exchange:
            return nums
    # return nums


print(f3())


def f4():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{} x {} = {}'.format(i, j, i * j), end='   ')
        print('\n')


# f4()

def fibnacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibnacci(n - 1) + fibnacci(n - 2)


# print(fibnacci(10))

# num = input('input 5 nums:')
# res = []
# for i in num.split():
#     res.append(int(i))
# print(res)


def f5(m, n):
    # 最大公约数
    def gcd(m, n):
        while n > 0:
            r = m % n
            m = n
            n = r
        return m

    x = gcd(m, n)
    y = m * n // x
    print('最大公约数是:', x)
    print('最小公倍数是:', y)
    # 最小公倍数


print(f5(21, 12))


# 输入整数n，输出1到n之间(包含n)所有素数的个数。
def f(n):
    count = 0
    res = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                # count += 1
                #                 print('{}不是素数'.format(i,))
                break
        else:
            count += 1
            res.append(i)
    print(res, count)
    return count  # 素数是大于1的数年所以要减去1个


# n = int(input('请输入n的值：'))
print('素数的个数为：{}'.format(f(10)))

'''
Sn= 1＋1／2＋1／3＋…＋1／n。显然对于任意一个整数K，当n足够大的时候，Sn大于K。
现给出一个整数K（1<=k<=15），要求计算出一个最小的n；使得Sn＞K。键盘输入 K，屏幕输出 n。
'''
def f7(k):
    sn = 0
    n = 1
    if k>=1 and k<=15:
        while True:
            sn += 1/n
            if sn > k:
                break
            n += 1


    print(sn, n)
f7(1)
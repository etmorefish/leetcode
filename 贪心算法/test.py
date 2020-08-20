import functools


def cmp(a, b):
    str1 = str(a) + str(b)
    str2 = str(b) + str(a)
    if str1 > str2:
        return 1
    elif str1 < str2:
        return -1
    else:
        return 0


if __name__ == '__main__':
    nums = [1, 3, 20, 15]
    nums.sort(key=functools.cmp_to_key(cmp))
    print(nums)

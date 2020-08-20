"""
假设商店老老老板需要找零n元钱,钱币的面面额有:100元、50元、
20元、5元、1元,如何找零使得所需钱币的数量量最少?

"""
t = [100, 50, 20, 5, 1]  # 钱币面额


def change(t, n):
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n = n % money
    return m, n


print(change(t, 378))  # ([3, 1, 1, 1, 3], 0)

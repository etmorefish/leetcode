"""
欧几几里里里得算法
欧几几里里里得算法:gcd(a, b) = gcd(b, a mod b)
例例:gcd(60, 21) = gcd(21, 18) = gcd(18, 3) = gcd(3, 0) = 3
"""


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcd2(a, b):
    while b>0:
        r = a%b
        a = b
        b = r
    return a


print(gcd(12, 20))
print(gcd2(12, 20))

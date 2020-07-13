import time

def two(func):
    def wrapper(*args, **kwargs):
        func.__name__ = input()
        func.__version__ = input()
        t1 = time.time()
        ret = func(*args, **kwargs)
        t2 = time.time()
        print(func.__name__, func.__version__, t2-t1)
        return ret
    return wrapper


@two
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None


# li = [1,2,3,4,5,6,7,8,9]
li = list(range(10000))
print(binary_search(li, 9323))
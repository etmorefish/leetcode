import random
import time


def running_time(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print('%s running time: %s secs.' % (func.__name__, t2 - t1))
        return res

    return inner


@running_time
def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li


def select_sort_simple(li):
    new_li = []
    for i in range(len(li)):
        min_val = min(li)
        new_li.append(min_val)
        li.remove(min_val)
    return new_li


@running_time
def select_sort(li):
    for i in range(len(li) - 1):
        min_index = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_index]:
                min_index = j
        li[i], li[min_index] = li[min_index], li[i]
    return li


# 快排，方案一 这种写法的平均空间复杂度为 O(nlogn)
def quick_sorts(li):
    if len(li) < 2:
        return li
    else:
        pivot = li[0]
        less = [i for i in li[1:] if i < pivot]
        greater = [i for i in li[1:] if i > pivot]
        return quick_sorts(less) + [pivot] + quick_sorts(greater)


# 快排，方案二
def quick_sort(li, left, right):
    def partition(li, left, right):
        tmp = li[left]
        while left < right:
            while left < right and li[right] >= tmp:
                right -= 1
            li[left] = li[right]
            # print(li)
            while left < right and li[left] <= tmp:
                left += 1
            li[right] = li[left]
            # print(li)
        li[left] = tmp
        return left

    if left < right:
        index = partition(li, left, right)
        quick_sort(li, left, index-1)
        quick_sort(li, index+1, right)
    return li

# 二分查找
def binary_search(li, val):
    left = 0
    right = len(li) -1
    while left <= right:
        mid = (left + right)//2
        if li[mid] == val:
            return True
        elif li[mid] > val:
            right = mid -1
        else:
            left = mid + 1
    else:
        None


def qs(li, l, r):
    def partition(li, l, r):
        pv = li[l]
        while l < r:
            while l< r and li[r] >= pv:
                r -= 1
            li[l] = li[r]
            while l < r and li[l] <= pv:
                l += 1
            li[r] = li[l]
        li[l] = pv
        return l
    if l < r:
        tmp = partition(li, l, r)
        qs(li, l, tmp -1)
        qs(li, tmp+1, r)
    return li



li = list(range(100))
random.shuffle(li)
print(li)
# print(bubble_sort(li))
# print(select_sort_simple(li))
# print(select_sort(li))
# print(quick_sorts(li))
# print(partition(li,0,len(li)-1))
# print(quick_sort(li, 0, len(li)-1))
# print(binary_search(quick_sort(li, 0, len(li)-1), 55))
print(qs(li, 0, len(li)-1))
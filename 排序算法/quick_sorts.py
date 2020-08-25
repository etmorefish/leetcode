import sys

sys.setrecursionlimit(100000)


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        # print(li, 'right')
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
        # print(li, 'left')
    li[left] = tmp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)
    return li

a = [0,0,1,2,4,2,2,3,1,4]
li = [6, 8, 3, 2, 9, 1]
# partition(li, 0, len(li)-1)
# print(li)
# quick_sort(li, 0, len(li) - 1)
# print(li)
# print(a)
print(quick_sort(a, 0, len(a) - 1))

def quick_sorts(li):
    if len(li) < 2:
        return li
    else:
        pivot = li[0]
        less = [i for i in li[1:] if i < pivot]
        greater = [j for j in li[1:] if j > pivot]
        return quick_sorts(less) + [pivot] + quick_sorts(greater)


# print(quick_sorts([1, 5, 2, 6, 9, 3]))
# print(quick_sorts([0,0,1,2,4,2,2,3,1,4]))

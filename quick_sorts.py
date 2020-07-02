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
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)


li = [6, 8, 3, 2, 9, 1]
# partition(li, 0, len(li)-1)
# print(li)
quick_sort(li, 0, len(li)-1)
print(li)

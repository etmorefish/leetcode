# https://zhuanlan.zhihu.com/p/57270323


class Solution(object):
    '''冒泡排序 O(n²)
    列表每两个相邻的数，如果前面比后面大，则交换这两个数
    一趟排序完成后，则无序区减少一个数，有序区增加一个数
    '''

    def bubbleSort(self, arr):
        length = len(arr)
        for i in range(length - 1):
            exchange = False      # 设立标志位 优化
            for j in range(length - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    exchange = True
        if not exchange:  # 优化，如果一趟没有发生交换，则说明列表已经有序，结束
            return arr
        # return arr

    '''选择排序
    无论什么数据进去都是 O(n²) 的时间复杂度
    数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。

    '''

    def selectSort(self, arr):
        length = len(arr)
        for i in range(length - 1):
            min = i
            for j in range(i + 1, length):
                if arr[j] < arr[min]:
                    min = j
                    arr[i], arr[min] = arr[min], arr[i]
        return arr

    '''插入排序
    '''

    def insertSort(self, arr):
        length = len(arr)
        for i in range(1, length):
            j = i - 1
            key = arr[i]
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                arr[j] = key
                j -= 1
        return arr


if __name__ == '__main__':
    arr = [6, 8, 3, 2, 9, 1]
    s = Solution()
    print(s.bubbleSort(arr))
    # print(s.selectSort(arr))
    # print(s.insertSort(arr))
    '''快速排序
    '''


    def partition(arr, low, high):
        i = (low-1)         # 最小元素索引
        pivot = arr[high]

        for j in range(low, high):

        # 当前元素小于或等于 pivot
            if arr[j] <= pivot:

                i = i+1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)


    # arr[] --> 排序数组
    # low  --> 起始索引
    # high  --> 结束索引

    # 快速排序函数
    def quickSort(arr, low, high):
        if low < high:

            pi = partition(arr, low, high)

            quickSort(arr, low, pi-1)
            quickSort(arr, pi+1, high)

    quickSort(arr, 0, 5)
    print(arr)



#  二分查找   
def birnary_search(li, val):
    l, r = 0 , len(li)-1
    while r > l:
        mid = (l+r)//2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            r = mid -1
        else:
            l = mid +1
    else:
        return None

# 装饰器   代码运行时间
import time

def run_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print('%s running %ss'%(func.__name__, t2-t1))
        return res
    return wrapper

    

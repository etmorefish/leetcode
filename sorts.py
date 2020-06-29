# https://zhuanlan.zhihu.com/p/57270323

class Solution(object):
    '''冒泡排序
    '''

    def bubbleSort(self, arr):
        length = len(arr)
        for i in range(length - 1):
            for j in range(length - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

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
    # print(s.bubbleSort(arr))
    # print(s.selectSort(arr))
    # print(s.insertSort(arr))
    a = 'aaabbc'
    b = 'a'
    c = 'rr'
    d = a.replace(b, c)
    print(d)
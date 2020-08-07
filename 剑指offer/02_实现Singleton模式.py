""" 单例设计模式
提高代码复用性
让类创建的对象，在内存中只有唯一的一个实例
new 为对象分配内存空间 返回对象引用
init 对象初始化 定义实例属性
"""


class Singleton:
    __obj = None
    __flag = False

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = super().__new__(cls)
        return cls.__obj

    def __init__(self):
        if not self.__flag:
            print('init····')
            self.__flag = True


a = Singleton()
b = Singleton()
print(a)
print(b)

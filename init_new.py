class A:
    def __init__(self):
        print('this is init method', self)

    def __new__(cls):
        print('this is cls`s id', id(cls))
        print('this is new method', object.__new__(cls))
        return object.__new__(cls)

a = A()
print('this is Class A of id', id(A))
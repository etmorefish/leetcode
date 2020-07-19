import time
from functools import wraps

def cal_time(func):
    def wrapper(*arg, **kwargs):
        t1 = time.time()
        result = func(*arg, **kwargs)
        t2 = time.time()
        print('%s running time: %s secs.'%(func.__name__, t2 - t1))
        return result
    return wrapper





def timerunning(func):
    @wraps(func)
    def inner(*args, **kwargs):
        t1 = time.time()
        ret = func(*args, **kwargs)
        t2 = time.time()
        print('running time: {}'.format(t2 - t1))
        return ret

    return inner

@cal_time
def f():
    time.sleep(0.5)
    print('f')
f()
print(f.__name__)

@timerunning
def f1():
    time.sleep(0.4)
    print('f1')
f1()
print(f1.__name__)
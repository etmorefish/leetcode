import time

def cal_time(func):
    def wrapper(*arg, **kwargs):
        t1 = time.time()
        result = func(*arg, **kwargs)
        t2 = time.time()
        print('%s running time: %s secs.'%(func.__name__, t2 - t1))
        return result
    return wrapper
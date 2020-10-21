import time

from .app import app


@app.task
def add(x, y):
    for i in range(5):
        time.sleep(1)
        print(f'-------{i}')
    return x + y
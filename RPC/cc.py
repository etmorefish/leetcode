import logging
import os
from logging import handlers

import time
from celery import Celery

broker = 'redis://127.0.0.1:6379'
# backend = 'redis://127.0.0.1:6379/0'

app = Celery('my_task', broker=broker)


import logging
import re
from logging.handlers import TimedRotatingFileHandler

LOG_FORMAT = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
log_path = 'logs/run_log.log'

# 每分钟生成一个日志文件   只保存4个日志文件
logger = TimedRotatingFileHandler(log_path, when="M", interval=1, backupCount=10, encoding='utf-8')
# logger.suffix = "%Y-%m-%d_%H-%M-%S.log"
logger.suffix = "%Y-%m-%d_%H-%M.log"
# 一定要与suffix对应，否则过期文件不会删除
# logger.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}.log$")
logger.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
logger.setFormatter(logging.Formatter(LOG_FORMAT))
# debug 以上的内容输出到文件里面
logger.setLevel('DEBUG')
logger.setLevel(logging.INFO)
log = logging.getLogger()
# log.setLevel('DEBUG')
# log.addHandler(logger)
# 将日志内容也输出到运行界面
# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)
# console.setFormatter(logging.Formatter(LOG_FORMAT))
# log.addHandler(console)

@app.task
def add(x, y):
    for i in range(6):
        time.sleep(1)
        print(f'-------{i}')
        # log.info(f'-------{i}')

        # logger.info('************')
    log.addHandler(logger)
    return x + y
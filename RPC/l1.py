import logging
import re
from logging.handlers import TimedRotatingFileHandler

LOG_FORMAT = "%(asctime)s=====%(levelname)s=====%(message)s"
log_path = 'logs/run_log.log'

# 每分钟生成一个日志文件   只保存4个日志文件
logger = TimedRotatingFileHandler(log_path, when="S", interval=1, backupCount=10, encoding='utf-8')
logger.suffix = "%Y-%m-%d_%H-%M-%S.log"
# 一定要与suffix对应，否则过期文件不会删除
logger.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}.log$")
logger.setFormatter(logging.Formatter(LOG_FORMAT))
# debug 以上的内容输出到文件里面
# logger.setLevel('DEBUG')
logger.setLevel(logging.DEBUG)
log = logging.getLogger()
log.setLevel('DEBUG')
log.addHandler(logger)
# 将日志内容也输出到运行界面
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(logging.Formatter(LOG_FORMAT))
log.addHandler(console)
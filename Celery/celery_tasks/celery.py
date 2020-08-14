# from celery import Celery
#
# cel = Celery('celery_demo',
#              broker='redis://127.0.0.1:6379/1',
#              backend='redis://127.0.0.1:6379/2',
#              # 包含以下两个任务文件，去相应的py文件中找任务，对多个任务做分类
#              include=['celery_tasks.task01',
#                       'celery_tasks.task02'
#                       ])
#
# # 时区
# cel.conf.timezone = 'Asia/Shanghai'
# # 是否使用UTC
# cel.conf.enable_utc = False


# celery worker -A celery_tasks -l info -P eventlet

# 定时
from datetime import timedelta
from celery import Celery
from celery.schedules import crontab

cel = Celery('tasks',
             broker='redis://127.0.0.1:6379/1',
             backend='redis://127.0.0.1:6379/2',
             include=[
                 'celery_tasks.task01',
                 'celery_tasks.task02',
             ])
cel.conf.timezone = 'Asia/Shanghai'
cel.conf.enable_utc = False

cel.conf.beat_schedule = {
    # 名字随意命名
    'add-every-10-seconds': {
        # 执行tasks1下的test_celery函数
        'task': 'celery_tasks.task01.send_email',
        # 每隔2秒执行一次
        # 'schedule': 1.0,
        # 'schedule': crontab(minute="*/1"),
        'schedule': timedelta(seconds=6),
        # 传递参数
        'args': ('张三',)
    },
    # 'add-every-12-seconds': {
    #     'task': 'celery_tasks.task01.send_email',
    #     每年4月11号，8点42分执行
    #     'schedule': crontab(minute=42, hour=8, day_of_month=11, month_of_year=4),
    #     'args': ('张三',)
    # },
}


# 启动 Beat 程序$ celery beat -A proj<br>
# Celery Beat进程会读取配置文件的内容，周期性的将配置中到期需要执行的任务发送给任务队列

# 之后启动 worker 进程.$ celery -A proj worker -l info 或者$ celery -B -A proj worker -l info
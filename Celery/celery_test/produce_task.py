# from celery_task import send_email
# result = send_email.delay("yuan")
# print(result.id)
# result2 = send_email.delay("alex")
# print(result2.id)

# 定时任务
from celery_task import send_email
from datetime import datetime

# 方式一
# v1 = datetime(2020, 8, 14, 11, 5, 00)
# print(v1)
# v2 = datetime.utcfromtimestamp(v1.timestamp())
# print(v2)
# result = send_email.apply_async(args=["egon",], eta=v2)
# print(result.id)

# 方式二
ctime = datetime.now()
# 默认用utc时间
utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
from datetime import timedelta
time_delay = timedelta(seconds=10)
task_time = utc_ctime + time_delay

# 使用apply_async并设定时间
result = send_email.apply_async(args=["egon"], eta=task_time)
print(result.id)
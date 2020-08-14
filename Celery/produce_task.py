from celery_tasks.task01 import send_email
from celery_tasks.task02 import send_msg

# 立即告知celery去执行test_celery任务，并传入一个参数
result = send_email.delay('xxml')
print(result.id)
result = send_msg.delay('xxml')
print(result.id)




# celery worker -A celery_task -l info -P eventlet
# BROKER_URL = 'redis://localhost:6379/1'     # 配置消息队列，默认使用 RabbitMQ
# BROKER_URL = 'amqp://dongwm:123456@localhost:5672/web_develop' # 使用RabbitMQ作为消息代理，默认地址 'amqp://guest:**@127.0.0.1:5672/'
CELERY_BROKER_URL = 'redis://localhost:6379/2'  # 把任务结果存在了Redis 区分生成的key，使用不同的库，使用 keys * 查看 # 把任务结果存在了Redis
CELERY_RESULT_BACKEND = 'redis://localhost:6379/3'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'           # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24   # 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显
CELERY_ACCEPT_CONTENT = ["json"]            # 指定任务接受的内容类型


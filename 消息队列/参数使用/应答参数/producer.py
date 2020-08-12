import pika

# 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 创建队列
channel.queue_declare(queue='hello')

# 向指定队列插入数据
channel.basic_publish(exchange='',    # 简单模式
                      routing_key='hello',  # 指定队列
                      body='Hello World!')  # 插入数据

print(" [x] Sent 'Hello World!'")
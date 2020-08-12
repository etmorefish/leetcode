import pika

# 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 创建持久化队列
channel.queue_declare(queue='hello5', durable=True)   # 若声明过，则换一个名字

# 向指定队列插入数据
channel.basic_publish(exchange='',    # 简单模式
                      routing_key='hello5',  # 指定队列
                      body='Hello World! 62',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      )
                      )  # 插入数据

print(" [x] Sent 'Hello World!'")
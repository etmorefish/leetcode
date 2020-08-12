import pika

# 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 申明交换机
channel.exchange_declare(exchange='logs2',
                         exchange_type='direct')   #


# 向指定交换机插入数据
message = "info: Hello World!"
channel.basic_publish(exchange='logs2',
                      routing_key='warring',
                      body=message)  # 插入数据

print(" [x] Sent %r" % message)
connection.close()
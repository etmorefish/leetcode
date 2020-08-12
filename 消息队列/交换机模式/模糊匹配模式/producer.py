import pika

# 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 申明交换机
channel.exchange_declare(exchange='logs3',
                         exchange_type='topic')   #


# 向指定交换机插入数据
message = "info: europe.news!"
channel.basic_publish(exchange='logs3',
                      routing_key='europe.news',
                      body=message)  # 插入数据

print(" [x] Sent %r" % message)
connection.close()
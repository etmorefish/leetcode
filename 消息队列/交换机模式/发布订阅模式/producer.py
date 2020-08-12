import pika

# 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 申明交换机
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')   # fanout：发布订阅模式参数


# 向指定交换机插入数据
message = "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)  # 插入数据

print(" [x] Sent %r" % message)
connection.close()
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 申明交换机
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')  # fanout：发布订阅模式参数

# 创建队列
result = channel.queue_declare("", exclusive=True)
queue_name = result.method.queue
print(queue_name)

# 将指定队列绑定交换机
channel.queue_bind(exchange='logs',
                   queue=queue_name)


# 确定回调函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# 确定监听队列
channel.basic_consume(queue=queue_name,
                      auto_ack=True,  # 默认应答
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
# 正式监听
channel.start_consuming()

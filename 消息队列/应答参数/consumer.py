import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 创建队列
channel.queue_declare(queue='hello')


# 确定回调函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 等待任务执行完、手动删除队列数据


# 确定监听队列
channel.basic_consume(queue='hello',
                      auto_ack=False,  # 默认应答 改为手动应答 队列数据不会删除
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
# 正式监听
channel.start_consuming()

import queue

q = queue.Queue(maxsize=10)

q.put(11)
q.put(22)
q.put(33)

print(q.get())
print(q.get())
print(q.get())
print(q.get(block=False))  # block  True：阻塞

import redis

r = redis.Redis(host='localhost', port=6379, db=1)

# print(r.keys())
for i in r.lrange('celery', 0, -1):
    print(i)
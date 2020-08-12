import rpyc

# 参数主要是host, port
conn = rpyc.connect('localhost', 9999)
# test是服务端的那个以"exposed_"开头的方法
print('start')
for i in range(100):
    cResult = conn.root.cal(i)
    print(cResult)
print('end')

conn.close()
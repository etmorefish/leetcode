import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8888))
sk.listen()

while True:
    conn, addr = sk.accept()
    data = conn.recv(8096)
    print(data)  # 将浏览器发来的消息打印出来
    conn.send(b"OK")
    conn.close()
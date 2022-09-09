# 网上搜的简单UDP服务端。待优化
import socket

addr = ('127.0.0.1', 4444)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(addr)

while True:
    print("listen")
    data, addr = s.recvfrom(4096)
    print(data, addr)

s.close()
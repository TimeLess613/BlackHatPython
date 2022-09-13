import socket

def sendto(host="127.0.0.1", port=9997):
    # object. datagram socket(SOCK_DGRAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # sent data
    client.sendto(b"AAAA", (host, port))

    # receive data
    # data, addr = client.recvfrom(4096)
    # print(data.decode(), addr)

    data_addr = client.recvfrom(4096)
    print(data_addr)

    client.close()

if __name__ == '__main__':
    # target_host = "127.0.0.1"
    target_host = "10.10.10.28"
    target_port = 4444
    sendto(target_host, target_port)


####### 踩坑 ########
# 1.打完代码直接运行后报错如下：
# ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。
# 应该是没有监听目标端口，但是搜索如何开启端口都是FW的教程。
# 于是找了个简单的UDP服务端代码，
# 先运行UDP服务端开启监听，然后再运行这个代码就成功了。
# ---
# 由于测试都是在windows所以之前想着用上面的方法。
# 后来想到我有虚拟机装了linux，其实可以用nc开启udp监听。
# 尝试后发现只能接受第一个udp包，
# 原因：https://www.markhneedham.com/blog/2013/07/30/netcat-strange-behaviour-with-udp-only-receives-first-packet-sent/
#
# 2.客户端、服务端的代码运行后无法用Ctrl+C、Ctrl+Z中断：
# 用Ctrl+Break即可。

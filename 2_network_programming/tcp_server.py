import socket
import threading
import time

def tcp_server(ip, port):
    # socket object with IPv4 and TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # listener， max connection 5.
    s.bind((bind_ip, bind_port))    
    s.listen(5)
    print(f"[*] Listening on {bind_ip}:{bind_port}")

    while True:
        # listener，wait for connection, save the object client to var client
        ## accept()会等待并返回一个客户端的连接（tuple）
        client, addr = s.accept()

        # creat new thread, handle_client().
        # spin up our client thread to handle/receive incoming data
        ## 之前的socket对象是第一个socket，
        ## 下面这里是复制之前的对象新建的socket来处理连接（大概）
        t = threading.Thread(target=handle_client, args=(client, addr))
        t.start()

# this is our client handling thread
## 由于会有多个客户端访问，所以每个连接都需要一个新的进程/线程来处理，否则，服务器一次就只能服务一个客户端了。
def handle_client(client_socket, addr):
    print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")

    # 似乎又是只接收一次。接收完就关闭当前线程
    with client_socket as sock:
        request = sock.recv(1024)
        # print out what the client sends
        print(f"[*] Received: \r\n{request.decode('utf-8')}")
        # send back a packet
        sock.send(b'ACK')

    # # 全接收的循环？
    # while True:
    #     data = client_socket.recv(1024)
    #     print(f"[*] Received: \r\n{data.decode('utf-8')}")
    #     client_socket.send(b'ACK')
    #     time.sleep(1)
    #     if not data or data.decode('utf-8')=='exit':
    #         break
    # client_socket.close()


if __name__ == "__main__":
    bind_ip = "127.0.0.1"
    bind_port = 4444
    tcp_server(bind_ip, bind_port)

import socket
import threading

def main():
    bind_ip = "0.0.0.0"
    bind_port = 4444
    
    # socket object with IPv4 and TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # listener，max connection 5.
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print(f"[*] Listening on {bind_ip}:{bind_port}")
    # print "[*] Listening on %s:%d" % (bind_ip, bind_port)

    while True:
        # wait for connection, save the object client to var client
        ## accept()会等待并返回一个客户端的连接
        client, addr = server.accept()
        print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")

        # creat new thread, handle_client().
        # spin up our client thread to handle/receive incoming data
        t = threading.Thread(target=handle_client, args=(client, addr))
        t.start()

# this is our client handling thread
## 由于会有多个客户端访问，所以每个连接都需要一个新的进程/线程来处理，否则，服务器一次就只能服务一个客户端了。
def handle_client(client_socket, addr):
    with client_socket as sock:
        # 似乎又是只接收一次。
        request = sock.recv(1024)

        # print out what the client sends
        print(f"[*] Received: {request.decode('utf-8')}")
        # send back a packet
        sock.send(b'ACK')


if __name__ == "__main__":
    main()

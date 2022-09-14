import socket

def udp_server(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((bind_ip, bind_port))
    print(f"[*] Listening on {bind_ip}:{bind_port}")

    while True:
        data, addr = s.recvfrom(1024)
        print(f'[*] Message from {addr[0]}:{addr[1]} : ', data.decode())
        s.sendto(f'Hello, {addr}'.encode(), addr)
    s.close()


if __name__ == '__main__':
    bind_ip = "127.0.0.1"
    bind_port = 4444
    udp_server(bind_ip, bind_port)
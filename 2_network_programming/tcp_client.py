import socket

def tcp_client(host, port):
    # socket object with IPv4 and TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect
    s.connect((host, port))

    # sent data
    ## 相关知识：报头格式，编码
    s.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n")

    # receive data
    ## 这里仅接收了一次。每次最多接收1KB
    response = s.recv(1024)
    print(response.decode())

    ## 全接收需要while循环
    ## 但似乎HTTP/1.1默认"Connection:Keep-Alive"，
    ## 如果报头不加"Connection: close"，则下面的while循环不会立马结束。
    ## buffer里append接收到的每一个包，最后拼接到data。
    buffer = []
    i = 0
    while True:
        i = i + 1

        d = s.recv(1024)
        if d:
            print(i)
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    print(data.decode())

    s.close()
    # save_html(data)


def save_html(data):
    # string.split(separator, maxsplit)
    ## 因为header是以'\r\n\r\n'结尾。
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    with open('google.html', 'wb') as f:
        f.write(html)

if __name__ == '__main__':
    # host = "www.google.com"
    # port = 80
    host = "127.0.0.1"
    port = 4444
    tcp_client(host, port)

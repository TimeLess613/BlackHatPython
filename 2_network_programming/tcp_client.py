import socket

def connect(host, port):
    # socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect
    client.connect((host, port))
    # sent data
    ## 相关知识：报头格式，编码
    client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n")

    # receive data
    ## 仅接收了一次。每次最多接收1KB
    response = client.recv(1024)
    print(response.decode())

    ## 全接收需要while循环
    ## 但似乎HTTP/1.1默认"Connection:Keep-Alive"，
    ## 如果报头不加"Connection: close"，则下面的while循环不会立马结束。
    buffer = []
    i = 0
    while True:
        i = i + 1

        d = client.recv(1024)
        if d:
            print(i)
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    print(data.decode())


    client.close()
    # save_html(data)


def save_html(data):
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    with open('google.html', 'wb') as f:
        f.write(html)

if __name__ == '__main__':
    host = "www.google.com"
    port = 80
    connect(host, port)

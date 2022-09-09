import socket

def connect(host="www.google.com", port=80):
    # object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect
    client.connect((host, port))

    # sent data
    client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

    # receive data
    response = client.recv(4096)

    print(response.decode())
    client.close()

if __name__ == '__main__':
    target_host = "www.google.com"
    target_port = 80
    connect(target_host, target_port)

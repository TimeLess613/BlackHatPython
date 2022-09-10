import socket
import threading

def main():
    bind_ip = "0.0.0.0"
    bind_port = 4444

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print(f"[*] Listening on {bind_ip}:{bind_port}")
    # print "[*] Listening on %s:%d" % (bind_ip, bind_port)

    while True:
        # wait for connection, 
        # save the object client to var client
        client, addr = server.accept()
        print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")

        # creat new thread, handle_client().
        # spin up our client thread to handle/receive incoming data
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

# this is our client handling thread
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)

        # print out what the client sends
        print(f"[*] Received: {request}")
        # send back a packet
        sock.send(b'ACK')


if __name__ == "__main__":
    main()
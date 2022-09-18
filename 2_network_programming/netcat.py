import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()

def options():
    # Create a parser object
    parser = argparse.ArgumentParser(
        description='BlackHatPython Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''
            Example:
                netcat.py -t 192.168.1.10 -p 4444                              # connect to server
                netcat.py -t 192.168.1.10 -p 4444 -l -c                        # command shell
                netcat.py -t 192.168.1.10 -p 4444 -l -e=\"cat /etc/passwd\"      # execute command
                netcat.py -t 192.168.1.10 -p 4444 -l -u=mytest.txt             # upload file
                echo 'ABC' | ./netcat.py -t 192.168.1.10 -p 135                # echo text to server port 135
            ''')
        )
    
    # Add options into parser
    ## action='store_true', 如果命令执行时有该option，则为True。
    ## 默认action='store'，表示储存输入的参数。
    parser.add_argument('-c', '--command', action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', help='execute command')
    parser.add_argument('-l', '--listen', action='store_true', help='create a listener')
    parser.add_argument('-p', '--port', type=int, help='specified port')
    parser.add_argument('-t', '--target', default='127.0.0.1', help='specified IP')
    parser.add_argument('-u', '--upload', help='upload file')

    # 解析参数
    ## 调用parse_args()方法将上述参数转换为指定对象（此处为parser）的属性
    ## 即：parser的命名空间下有command、listen等属性（option）
    args = parser.parse_args()
    
    return args

class NetCat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()

    def listen():
        pass

    def send():
        self.socket.connect((self.args.t, self.args.p))
        if self.buffer:
            self.socket.send(self.buffer)

        try:
            while True:
                


if __name__ == '__main__':
    args = options()

    # 如果有listen参数/属性则为Ture（因为'store_true'）
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()


    nc = NetCat(args, buffer.encode())
    nc.run()
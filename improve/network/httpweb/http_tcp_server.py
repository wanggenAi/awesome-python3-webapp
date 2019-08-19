import socket

"""
    对于服务器和客户端来说，哪一方先调用close()方法，哪一端最后就会等待2-5分钟来等待是否有新的请求连接，
    最终释放资源，在服务端，如果先调用了close()方法，此时立刻再重启应用，就会出现address in used异常
    此时在创建完套接字对象后，可以设置这对象的参数，复用地址跟端口号
"""
def service_client(new_socket):
    # 接收客户端发送过来的数据 GET / HTTP/1.1
    request = new_socket.recv(1024)
    print(request)
    # 发送给客户端数据，有header跟body满足http协议的要求
    response = 'HTTP/1.1 200 ok\r\n'
    response += '\r\n'
    # 拼接Body数据
    response += "<h1>如果时间忘记了转</h1>"
    new_socket.send(response.encode("gbk"))
    new_socket.close()

def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定端口
    tcp_socket.bind(("", 7890))
    # 变为监听模式
    tcp_socket.listen(128)
    # 处理客户端请求，返回数据
    while True:
        # 接收客户端连接请求
        new_socket, client_addr = tcp_socket.accept()
        service_client(new_socket)


if __name__ == '__main__':
    main()
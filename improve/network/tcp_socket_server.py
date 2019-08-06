import socket

def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 绑定本地信息
    tcp_server_socket.bind(("",7890))
    # 默认主动变为被动
    tcp_server_socket.listen(128)

    while True:
        # 等待客户端的链接
        print("等待一个新客户端的到来...")
        client_socket,client_addr = tcp_server_socket.accept()
        print("一个新的客户端已经到来%s" % str(client_addr))
        # 为同一个客户端服务多次
        while True:
            # 接受客户端发送过来的请求
            recv_data = client_socket.recv(1024)
            # 如果recv解堵塞，有两种可能 1.客户端发送过来了数据，2.客户端调用了close，返回值就是None
            if not recv_data:
                break
            print("客户端发送过来的消息：%s" % recv_data.decode("gbk"))
            # 回送数据
            client_socket.send("hahah----ok".encode("gbk"))
        # 关闭套接字
        client_socket.close()
        print("服务完毕...")
    tcp_server_socket.close()

if __name__ == '__main__':
    main()
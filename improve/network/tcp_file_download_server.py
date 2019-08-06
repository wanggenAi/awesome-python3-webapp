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
            if send_file_2_client(client_socket,client_addr): break
        # 关闭套接字
        client_socket.close()
        print("服务完毕...")
    tcp_server_socket.close()


def send_file_2_client(client_socket,client_addr):
    filename = client_socket.recv(1024).decode("gbk")
    print("客户端(%s)需要下载的文件是：%s" % (str(client_addr), filename))

    file_content = None
    # 打开这个文件，读取数据  with只能保证写文件没问题，读如果没有文件依然会异常
    try:
        f = open(filename,'rb')
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件%s" % filename)

    # 将数据发送给客户端
    # 如果recv解堵塞，有两种可能 1.客户端发送过来了数据，2.客户端调用了close，返回值就是None
    if not filename:
        return True
    # 回送数据
    if file_content:
        client_socket.send(file_content)

if __name__ == '__main__':
    main()
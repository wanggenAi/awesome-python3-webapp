import socket

def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 输入服务器ip、端口
    dest_ip = "192.168.208.3"
    dest_port = 7890

    # 连接服务器
    tcp_socket.connect((dest_ip,dest_port))
    # 发送文件名请求
    filename = input("要下载的文件名：")
    tcp_socket.send(filename.encode("gbk"))

    # 获取服务器传来的信息
    recv_data = tcp_socket.recv(1024*1024)
    if recv_data:
        # 将信息写入本地文件中
        with open('复件'+filename,"wb") as f:
            f.write(recv_data)
        # 关闭套接字
        tcp_socket.close()


if __name__ == '__main__':
    main()
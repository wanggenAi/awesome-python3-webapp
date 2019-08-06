import socket

def main():
    # 创建TCP的套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 链接服务器
    server_ip = "192.168.110.106"
    server_port = 10000
    tcp_socket.connect((server_ip,server_port))
    # 发送接受数据
    send_data = input("请输入要发送的数据：")
    tcp_socket.send(send_data.encode("gbk"))

    # 关闭套接字
    tcp_socket.close()

if __name__ == '__main__':
    main()
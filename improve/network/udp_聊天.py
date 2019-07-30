import socket

def send_msg(udp_socket):
    """发送消息"""
    # 1. 发送
    send_data = input("请输入要发送的消息：")
    dest_ip = "192.168.110.106"
    dest_port = 10000
    udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))

def recv_msg(udp_socket):
    """接受数据"""
    # 2. 接收并显示
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("gbk")))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 绑定信息
    udp_socket.bind(("",9999))
    while True:
        send_msg(udp_socket)
        recv_msg(udp_socket)


if __name__ == '__main__':
    main()
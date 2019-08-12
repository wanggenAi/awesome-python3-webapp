import threading
import socket

def receive(udp_socket):
    # 接收数据
    while True:
        recv_date = udp_socket.recvfrom(1024)
        print(recv_date[0].decode("gbk"))


def sendto(udp_socket,dest_ip,dest_port):
    # 发送数据
    while True:
        send_msg = input("输入要发送的信息：")
        udp_socket.sendto(send_msg.encode("gbk"),(dest_ip,dest_port))


def main():
    """完成udp聊天器的整体控制"""
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 绑定本地信息
    udp_socket.bind(("",7890))
    # 获取对方的ip
    dest_ip = "192.168.110.106"
    dest_port = 8080
    recv = threading.Thread(target=receive, args=(udp_socket,))
    send = threading.Thread(target=sendto, args=(udp_socket,dest_ip,dest_port))
    recv.start()
    send.start()


if __name__ == '__main__':
    main()
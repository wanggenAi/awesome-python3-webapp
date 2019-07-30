import socket

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地
    udp_socket.bind(('',7890))

    # 可以使用套接字收发数据,发送任意数据给windows
    while True:
        send_data = input("请输入要发送的数据：")
        if send_data == 'exit':
            break
        udp_socket.sendto(send_data.encode("utf8"),('192.168.110.106',10000))
        # 关闭套接字



    udp_socket.close()

if __name__ == '__main__':
    main()
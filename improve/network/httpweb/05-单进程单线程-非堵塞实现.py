import socket
import time

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(("", 7890))
tcp_server.listen(128)
tcp_server.setblocking(False)

client_socket_list = list()


def main():
    while True:
        time.sleep(0.5)
        try:
            new_socket, client_addr = tcp_server.accept()
        except Exception as ret:
            print("------没有新的客户端到来------")
        else:
            client_socket_list.append(new_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024)
            except Exception as ret:
                print("该客户端没有数据发送")
            else:
                if recv_data:
                    print("客户端传来的数据是",recv_data)
                else:
                    # 客户端调用了close
                    client_socket_list.remove(client_socket)
                    client_socket.close()

if __name__ == '__main__':
    main()
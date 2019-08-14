import socket

def serivce_client(new_socket):
    """为这个客户端返回数据"""
    # 接收浏览器发送过来的请求， http请求 GET / HTTP/1.1
    request = new_socket.recv(1024)
    print(request)
    # 返回http格式的数据， 给浏览器
    # 准备发送给浏览器的header
    response = "HTTP/1.1 200 ok\r\n"
    # 准备发送给浏览器的body



def main():
    """用来完成整体的控制"""
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定
    tcp_socket.bind(("", 7890))
    # 变为监听套接字
    tcp_socket.listen(128)
    # 等待新客户端的链接
    new_socket, client_addr = tcp_socket.accept()
    # 为这个客户端服务
    serivce_client(new_socket)

if __name__ == '__main__':
    main()
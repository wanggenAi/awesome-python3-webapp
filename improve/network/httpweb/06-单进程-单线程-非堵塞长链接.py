import socket
import re
import select

def service_client(new_socket, request):
    request_lines = request.splitlines()
    print(request_lines)

    file_name = ""
    # GET /index.html
    ret = re.match(r"[^/]*(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

    try:
        f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "------------file not found-------------"
        new_socket.send(response.encode("gbk"))
    else:
        html_content = f.read()
        f.close()
        response_body = html_content
        response_header = "HTTP/1.1 200 ok\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        response = response_header.encode("gbk") + response_body
        new_socket.send(response)

def main():
    """用来完成整体控制"""
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定本地ip端口
    tcp_socket.bind(("", 7890))
    # 变为监听模式
    tcp_socket.listen(128)
    tcp_socket.setblocking(False)  # 将套接字变为非堵塞
    # 创建一个epoll对象
    epl = select.epoll()
    # 将监听套接字对应的fd放入共享内存中
    epl.register(tcp_socket.fileno(), select.EPOLLIN)
    # 接收客户端的连接请求
    # 处理用户的http请求，返回固定页面
    fd_event_dict = dict()
    while True:
        fd_event_list = epl.poll()  # 默认会堵塞，直到 os 检测到数据的到来 通过事件的通知方式，此时才会解堵塞

        # [(fd, event)] 套接字对应的文件描述符， 这个文件描述符到底是什么事件，例如可以调用receive接收等
        for fd, event in fd_event_list:
            if fd == tcp_socket.fileno():
                new_socket, client_addr = tcp_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                # 说明已经建立连接的套接字收取到了客户的数据，需要从字典里取出这个套接字，处理数据
                recv_data = fd_event_dict[fd].recv(1024).decode("gbk")
                if recv_data:
                    service_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]


if __name__ == '__main__':
    main()
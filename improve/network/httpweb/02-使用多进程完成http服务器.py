import socket
import re
import threading

def service_client(new_socket):
    # 接收客户端发来的request请求 GET / HTTP/1.1
    request = new_socket.recv(1024).decode("gbk")
    # print(request)
    # 返回固定的页面
    request_lines = request.splitlines()
    print(">"*20)
    print(request_lines)
    # GET /index.html HTTP/1.1
    file_name = ""
    try:
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if ret:
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "/index.html"
            print(file_name)
        # 打开html文件
        f = open("./html"+file_name, "rb")
        html_content = f.read()
        f.close()
        response = "HTTP/1.1 200 ok\r\n"
        response += "\r\n"
        new_socket.send(response.encode("gbk"))
        new_socket.send(html_content)
        new_socket.close()
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "------------file not found--------"
        new_socket.send(response.encode("gbk"))
        new_socket.close()




def main():
    """用来完成整体控制"""
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定本地ip端口
    tcp_socket.bind(("", 7890))
    # 变为监听模式
    tcp_socket.listen(128)
    # 接收客户端的连接请求
    # 处理用户的http请求，返回固定页面
    while True:
        new_socket, client_addr = tcp_socket.accept()
        # 为这个客户端服务
        p = threading.Thread(target=service_client, args=(new_socket,))
        p.start()

if __name__ == '__main__':
    main()
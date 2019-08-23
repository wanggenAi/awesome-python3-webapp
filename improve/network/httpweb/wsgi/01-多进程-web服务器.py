import socket
import re
import multiprocessing


class WSGIServer(object):
    def __init__(self):
        # 创建套接字
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定本地ip端口
        self.tcp_socket.bind(("", 7890))
        # 变为监听模式
        self.tcp_socket.listen(128)
        # 接收客户端的连接请求
        # 处理用户的http请求，返回固定页面

    def service_client(self, new_socket):
        # 接收客户端发来的request请求 GET / HTTP/1.1
        request = new_socket.recv(1024).decode("gbk")
        # print(request)
        # 返回固定的页面
        request_lines = request.splitlines()
        print(">" * 20)
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
            f = open("../html" + file_name, "rb")
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

    def run_forever(self):
        """用来完成整体控制"""
        while True:
            new_socket, client_addr = self.tcp_socket.accept()
            # 为这个客户端服务
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()
            new_socket.close()




if __name__ == '__main__':
    """控制整体，创建一个web服务器对象,调用对象的run_forever方法运行"""
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()
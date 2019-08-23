import socket
import re
import multiprocessing
from dynamic import wsgi_mini_frame
import sys


class WSGIServer(object):
    def __init__(self, port, app, config_info):
        # 创建套接字
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定本地ip端口
        self.tcp_socket.bind(("", port))
        # 变为监听模式
        self.tcp_socket.listen(128)
        self.application= app
        self.config_info = config_info
        # 接收客户端的连接请求
        # 处理用户的http请求，返回固定页面

    def service_client(self, new_socket):
        # 接收客户端发来的request请求 GET / HTTP/1.1
        request = new_socket.recv(1024).decode("utf-8")
        # print(request)
        # 返回固定的页面
        request_lines = request.splitlines()
        print(">" * 20)
        print(request_lines)
        # GET /index.html HTTP/1.1
        file_name = ""
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if ret:
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "/index.py"
            print(file_name)
        # 如果请求的资源不是以py结尾，则是静态资源
        if not file_name.endswith(".py"):
                # 打开html文件
            try:
                print(self.config_info["static_path"])
                f = open(self.config_info["static_path"] + file_name, "rb")
                html_content = f.read()
                f.close()
                response = "HTTP/1.1 200 ok\r\n"
                response += "\r\n"
                new_socket.send(response.encode("utf-8"))
                new_socket.send(html_content)
                new_socket.close()
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "------------file not found--------"
                new_socket.send(response.encode("utf-8"))
        else:
            # 如果是以.py结果，则是动态资源的请求
            # body =  mini_frame.login()
            env = dict()
            env['PATH_INFO'] = file_name
            body = self.application(env, self.set_response_header)
            header = "HTTP/1.1 %s\r\n" % self.status
            self.headers += [('server', 'mini_frame v999'),]
            for temp in self.headers:
                header += '%s:%s\r\n' % (temp[0], temp[1])

            header += "\r\n"
            response = header + body
            # 发送response给浏览器
            new_socket.send(response.encode("utf-8"))
        new_socket.close()

    def set_response_header(self, status, headers):
        self.status = status
        self.headers = headers

    def run_forever(self):
        """用来完成整体控制"""
        while True:
            new_socket, client_addr = self.tcp_socket.accept()
            # 为这个客户端服务
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()
            new_socket.close()

def main():
    """控制整体，创建一个web服务器对象,调用对象的run_forever方法运行"""
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1]) # 7890
            frame_app_name = sys.argv[2] # mini_frame:application
            ret = re.match(r'([^:]+):(.*)', frame_app_name)
            if ret:
                frame_name = ret.group(1)  # mini_frame
                app_name = ret.group(2)  # application
            else:
                print("请按照以下方式运行")
                print("python3 xxx.py 7890 mini_frame:application")
                return
        except Exception as ret:
            print("端口输入错误")
            return
    else:
        print("请按照以下方式运行")
        print("python3 xxx.py 7890")
        return

    # mini_frame:application

    # import frame_name --------> 找的是frame_name模块，没有的
    with open("./web_server.conf") as f:
       config_info = eval(f.read())

    sys.path.append(config_info["dynamic_path"])
    frame = __import__(frame_name) # 返回值是导入的模块对象
    app = getattr(frame, app_name) # app就指向了dynamic下的mini_frame模块下的application这个函数
    wsgi_server = WSGIServer(port, app, config_info)
    wsgi_server.run_forever()


if __name__ == '__main__':
    main()
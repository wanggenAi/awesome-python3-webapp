import time

def login():
    return "LOGINwelcome to our website.....time:%s" % time.ctime()

def register():
    return "REGISTERwelcome to our website.....time:%s" % time.ctime()

def profile():
    return "PROFILEwelcome to our website.....time:%s" % time.ctime()

def index():
    return "这是mini_frame的首页site.....time:%s" % time.ctime()

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']
    if file_name == '/login.py':
        return login()
    elif file_name == '/register.py':
        return register()
    elif file_name == '/index.py':
        return index()
    else:
        return "not found your page..."
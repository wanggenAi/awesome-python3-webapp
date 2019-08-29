def set_func(func):
    print("-----开始进行装饰")
    def call_func(*args, **kwargs):
        print("-----这是前缀代码1------")
        print("-----这是前缀代码222------")
        func(*args, **kwargs)
    return call_func

@set_func
def test1(num, *args, **kwargs):
    print("------test1------%d" % num)
    print("------test1------", args)
    print("------test1------", kwargs)

test1(100)
test1(100, 200)
test1(100, 200, 300, mm=100)

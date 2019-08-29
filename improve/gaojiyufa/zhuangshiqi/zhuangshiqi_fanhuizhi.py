def set_func(func):
    print("-----开始进行装饰")
    def call_func(*args, **kwargs):
        print("-----这是前缀代码1------")
        print("-----这是前缀代码222------")
        return func(*args, **kwargs)
    return call_func

@set_func
def test1(num, *args, **kwargs):
    print("------test1------%d" % num)
    print("------test1------", args)
    print("------test1------", kwargs)
    return "ok"

ret = test1(100)
print(ret)

def set_func(func):
    print("ni adawda")
    def call_func():
        print("这是装饰器----")
        func(2, 33)
    return call_func

@set_func
def test(num1, num2):
    print("-------test----%d%d" % (num1, num2))


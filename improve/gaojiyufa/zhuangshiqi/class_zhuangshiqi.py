class Test(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("这是类装饰器会执行的方法")
        return self.func()



@Test    # 相当于 get_str = Test(get_str)
def get_str():
    return "haha"

print(get_str())   # 相当于调用了对象的__call__方法


def add_qx(func):
    print("----开始装饰quanxian的功能----")
    def call_func(*args, **kwargs):
        print("----这是quanxian认证-----")
        return func(*args, **kwargs) # 拆包
    return call_func

def add_xx(func):
    print("----开始装饰xxx的功能----")
    def call_func(*args, **kwargs):
        print("----这是xxxxx认证-----")
        return func(*args, **kwargs) # 拆包
    return call_func

@add_qx
@add_xx
def test():
    print("--------test--------")

test()

"""
    总结：当多个装饰器对于一个函数进行装饰的时候，首先执行最上面的程序，依次往下执行，而装饰的时候，首先装饰最下面的程序，
    依次往上装饰，因为他要把闭包的函数引用，往上传递，传递到最上层，然后再由最上层开始执行程序
"""
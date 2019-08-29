def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print("1级权限认证。。。")
            elif level_num == 2:
                print("2级权限认证....")
            return func(*args, **kwargs)
        return call_func
    return set_func


# 调用带参数的返回值有两步：
# 1. 调用set_func函数，并传递参数进去
# 2. 获取这个调用的函数的返回值，并用这个返回值来对原始函数进行装饰
@set_level(1)
def test1():
    print("---------test111----------")
    return "ok"

@set_level(2)
def test2():
    print("---------test222----------")
    return "ok"

test1()
test2()
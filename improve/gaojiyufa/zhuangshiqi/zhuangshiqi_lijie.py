import time
# def set_func(func):
#     def call_func():
#         print("这里是新添加的功能111111111")
#         print("这里是新添加的功能222222222222")
#         func()
#     return call_func
#
# @set_func
# def test1():
#     print("这是主程序需要执行的代码")
#
# test1()


def set_func(func):
    def call_func():
        print("这里是新添加的功能111111111")
        print("这里是新添加的功能222222222222")
        start_time = time.time()
        func()
        stop_time = time.time()
        print("alltimes %f" % (stop_time - start_time))
    return call_func

def test1():
    print("这是主程序需要执行的代码")
    for i in range(10000):
        pass

test1 = set_func(test1)
test1()



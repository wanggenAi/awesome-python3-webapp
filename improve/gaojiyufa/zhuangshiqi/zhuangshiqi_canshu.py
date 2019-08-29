

def set_func(func):
    def call_func(num):
        print("装饰器前面做的事情1")
        print("装饰器前面做的事情22222")
        func(3)
    return call_func

@set_func
def test(num):
    print("这是测试函数test----%d" % num)

def test2(num):
    print("测试函数test2-----%d" % num)

def main():
    print(id(test))
    print(id(test2))


if __name__ == '__main__':
    main()
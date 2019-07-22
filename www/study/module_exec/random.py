# 文件被导入，能够直接执行的代码不需要执行！


# 如果需要测试模块，就可以使用__name__内置属性来判断是否运行的是自己还是从其他模块中导入的

def main():
    print("random模块")

    def say_hello():
        print("你好，say hello")

    say_hello()

if __name__ == "__main__":
    main()